import os
from PIL import Image
from PIL.ExifTags import TAGS
from directory_functions import scan_directory
from tools import extract_gps_info

def get_exif_data(img_path):
    """Extract normalized EXIF metadata from an image and return as dictionary."""
    data = {
        "FileName": os.path.basename(img_path),
        "FilePath": img_path,
        "FileSize": None,
        "FileType": None,
        "Make": None,
        "Model": None,
        "Software": None,
        "ExifVersion": None,
        "DateTimeOriginal": None,
        "Width": None,
        "Height": None,
        "Latitude": None,
        "Longitude": None,
        "Altitude": None,
        "Orientation": None,
        "Properties": {}
    }

    try:
        # File info
        stat = os.stat(img_path)
        data["FileSize"] = stat.st_size
        data["FileType"] = os.path.splitext(img_path)[1].lower().strip(".")

        img = Image.open(img_path)
        info = img._getexif()

        if not info:
            return data

        exif_data = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif_data[decoded] = value

        # Core fields
        data["Make"] = exif_data.get("Make")
        data["Model"] = exif_data.get("Model")
        data["Software"] = exif_data.get("Software") or exif_data.get("ProcessingSoftware")
        data["ExifVersion"] = exif_data.get("ExifVersion")

        # Date handling
        data["DateTimeOriginal"] = (
            exif_data.get("DateTimeOriginal") or
            exif_data.get("DateTimeDigitized") or
            exif_data.get("DateTime")
        )

        # Dimensions
        data["Width"] = exif_data.get("ExifImageWidth") or exif_data.get("ImageWidth")
        data["Height"] = exif_data.get("ExifImageHeight") or exif_data.get("ImageLength")

        # Orientation
        data["Orientation"] = exif_data.get("Orientation")

        # GPS
        gps_info = exif_data.get("GPSInfo")
        gps = extract_gps_info(gps_info)
        data.update(gps)

        # Properties
        props = {
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
        data["Properties"] = {k: (v if v is not None else None) for k, v in props.items()}

    except Exception as e:
        print(f"Error reading {img_path}: {e}")

    return data

if __name__ == "__main__":
    folder = input("Enter folder path: ")
    scan_directory(folder, task=get_exif_data)
