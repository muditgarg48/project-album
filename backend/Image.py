# from database_functions import db

# class MediaDeviceOrigin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     make = db.Column(db.String, nullable=True)
#     model = db.Column(db.String, nullable=True)
#     software = db.Column(db.String, nullable=True)
#     exif_version = db.Column(db.String, nullable=True)

# class MediaProperties(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     width = db.Column(db.Integer, nullable=True)
#     height = db.Column(db.Integer, nullable=True)
#     properties = db.Column(db.JSON, nullable=True)

# class MediaLocation(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     latitude = db.Column(db.Float, nullable=True)
#     longitude = db.Column(db.Float, nullable=True)
#     altitude = db.Column(db.Float, nullable=True)

# class Image(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     file_name = db.Column(db.String, nullable=False)
#     file_path = db.Column(db.String, unique=True, nullable=False)
#     file_size = db.Column(db.Integer, nullable=True)
#     date_timestamp = db.Column(db.DateTime, nullable=True)
#     orientation = db.Column(db.Integer, nullable=True)
#     file_origin = db.relationship('MediaDeviceOrigin', backref='image', uselist=False)
#     location = db.relationship('MediaLocation', backref='image', uselist=False)
#     properties = db.relationship('MediaProperties', backref='image', uselist=False)

import os
from Face import Face
import cv2

from constants import IMAGE_EXTENSIONS

from PIL import Image as PILImage
from PIL.ExifTags import TAGS
from tools import extract_gps_info, face_detector

class Image():

    def __init__(self, file_path):
        
        # CHECKPOINT: File exists
        if not os.path.isfile(file_path):
            raise ValueError(f"File does not exist at {file_path}")
        file_extension = os.path.splitext(file_path)[1].lower()
        # CHECKPOINT: File is valid image
        if file_extension not in IMAGE_EXTENSIONS:
            raise ValueError(f"Unsupported image format: {file_extension}")
        
        # CHECKPOINT: Image object creation
        self.file_extension = file_extension
        self.file_path = file_path
        self.file_name = os.path.basename(self.file_path)
        self.file_size = os.stat(self.file_path).st_size
        self.date_timestamp = None
        self.orientation = None
        self.file_origin = None
        self.location = None
        self.properties = None
        self.faces = []
        self.set_img_data()
        self.detect_faces()

    def object_guide(self):
        return dir(self)

    # Getter methods
    def get_file_path(self):
        return self.file_path
    
    def get_file_name(self):
        return self.file_name
    
    def get_file_size(self):
        return self.file_size
    
    def get_date_timestamp(self):
        return self.date_timestamp
    
    def get_orientation(self):
        return self.orientation
    
    def get_file_origin(self):
        return self.file_origin
    
    def get_location(self):
        return self.location
    
    def get_properties(self):
        return self.properties
    
    def get_img_data(self):
        return {
            "FileName": self.file_name,
            "FilePath": self.file_path,
            "FileSize": self.file_size,
            "FileType": self.file_extension,
            "FileOrigin": self.file_origin,
            "DateTimeOriginal": self.date_timestamp,
            "Location": self.location,
            "Orientation": self.orientation,
            "Properties": self.properties
        }
    
    def show_img(self):
        cv2.namedWindow(self.file_name, cv2.WINDOW_NORMAL)
        img = cv2.imread(self.file_path)
        cv2.imshow(self.file_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def show_faces(self):
        window_name = f"{self.file_name} with {len(self.faces)} detected faces"
        cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        img = cv2.imread(self.file_path)
        for face in self.faces:
            face.show_face(img)
            face.show_keypoints(img)
        cv2.imshow(window_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Setter methods
    # def set_file_path(self, file_path):
    #     self.file_path = file_path

    # def set_file_name(self, file_name):
    #     self.file_name = file_name
    
    # def set_file_size(self, file_size):
    #     self.file_size = file_size

    def set_date_timestamp(self, date_timestamp):
        self.date_timestamp = date_timestamp
    
    def set_orientation(self, orientation):
        self.orientation = orientation
    
    def set_file_origin(self, file_origin):
        self.file_origin = file_origin
    
    def set_location(self, location):
        self.location = location
    
    def set_properties(self, properties):
        self.properties = properties
    
    def set_img_data(self):
        """Extract normalized EXIF metadata from an image and return as dictionary."""

        try:
            img = PILImage.open(self.file_path)
            info = img._getexif()

            if not info:
                return

            # Decode EXIF data from numeric tags to human-readable tags
            exif_data = {}
            for tag, value in info.items():
                decoded = TAGS.get(tag, tag)
                exif_data[decoded] = value

            # Date handling
            self.set_date_timestamp((
                exif_data.get("DateTimeOriginal") or
                exif_data.get("DateTimeDigitized") or
                exif_data.get("DateTime")
            ))

            # Orientation
            self.set_orientation(exif_data.get("Orientation"))

            # Image device origin
            file_origin = {}
            file_origin["Make"] = exif_data.get("Make")
            file_origin["Model"] = exif_data.get("Model")
            file_origin["Software"] = exif_data.get("Software") or exif_data.get("ProcessingSoftware")
            file_origin["ExifVersion"] = exif_data.get("ExifVersion")
            self.set_file_origin(file_origin)

            # GPS
            gps_info = exif_data.get("GPSInfo")
            gps = extract_gps_info(gps_info)
            self.set_location(gps)

            # Properties
            props = {
                "Width": exif_data.get("ExifImageWidth") or exif_data.get("ImageWidth"),
                "Height": exif_data.get("ExifImageHeight") or exif_data.get("ImageLength"),
                "FocalLength": exif_data.get("FocalLength"),
                "ExposureTime": exif_data.get("ExposureTime") or exif_data.get("ShutterSpeedValue"),
                "ApertureValue": exif_data.get("ApertureValue") or exif_data.get("MaxApertureValue"),
                "ISO": exif_data.get("ISOSpeedRatings") or exif_data.get("PhotographicSensitivity"),
                "FNumber": exif_data.get("FNumber"),
                "WhiteBalance": exif_data.get("WhiteBalance"),
                "DigitalZoomRatio": exif_data.get("DigitalZoomRatio"),
                "Contrast": exif_data.get("Contrast"),
                "Saturation": exif_data.get("Saturation"),
                "Sharpness": exif_data.get("Sharpness"),
                "BrightnessValue": exif_data.get("BrightnessValue"),
                "ColorSpace": exif_data.get("ColorSpace"),
            }
            self.set_properties({k: (v if v is not None else None) for k, v in props.items()})

        except Exception as e:
            raise Exception(f"Error decoding {self.file_path}: {e}")
    
    def add_face(self, face):
        # CHECKPOINT: Ensure face is an instance of Face class
        if isinstance(face, Face):
            self.faces.append(face)
        else:
            raise ValueError("Argument must be an instance of Face class")

    # Helper methods
    def detect_faces(self):
        img = cv2.imread(self.file_path)
        results = face_detector.detect_faces(img)
        for result in results:
            top_left_x, top_left_y, width, height = result['box']
            bottom_right_x = top_left_x + width
            bottom_right_y = top_left_y + height
            bounding_box = {
                "top_left": (top_left_x, top_left_y),
                "bottom_right": (bottom_right_x, bottom_right_y),
                "width": width,
                "height": height
            } 
            detected_face = Face(
                image_path=self.file_path,
                bounding_box=bounding_box,
                confidence=result['confidence'],
                keypoints=result.get('keypoints')
            )
            self.add_face(detected_face)
        print(f"Detected {len(self.faces)} faces within {self.file_name}")

    # Database functions
    # TO_DO: Implement database addition
    def add_img_to_db(self):
        pass