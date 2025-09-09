# from database_functions import db

# class Face(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     image_id = db.Column(db.Integer, db.ForeignKey('image.id'), nullable=False)
#     bounding_box = db.Column(db.JSON, nullable=False)
#     confidence = db.Column(db.Float, nullable=False)
#     keypoints = db.Column(db.JSON, nullable=True)
#     image = db.relationship('Image', backref=db.backref('faces', lazy=True))

import cv2

class Face():
    def __init__(self, image_path, bounding_box, confidence, keypoints=None):
        self.image_path = image_path
        self.bounding_box = bounding_box
        self.confidence = confidence
        self.keypoints = keypoints
    
    def object_guide(self):
        return dir(self)

    # Getter methods
    def get_image_path(self):
        return self.image_path
    
    def get_bounding_box(self):
        return self.bounding_box
    
    def get_confidence(self):
        return self.confidence
    
    def get_keypoints(self):
        return self.keypoints
    
    # Setter methods
    def set_image_path(self, image_path):
        self.image_path = image_path
    
    def set_bounding_box(self, bounding_box):
        self.bounding_box = bounding_box
    
    def set_confidence(self, confidence):
        self.confidence = confidence
    
    def set_keypoints(self, keypoints):
        self.keypoints = keypoints
    
    # Face hightlighter methods
    def show_face(self, img):
        cv2.rectangle(img, pt1=self.bounding_box["top_left"], pt2=self.bounding_box["bottom_right"], color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA, shift=0)
    
    def show_eyes(self, img):
        if self.keypoints and "left_eye" in self.keypoints and "right_eye" in self.keypoints:
            cv2.circle(img, center=self.keypoints["left_eye"], radius=3, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
            cv2.circle(img, center=self.keypoints["right_eye"], radius=3, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
    
    def show_mouth(self, img):
        if self.keypoints and "mouth_left" in self.keypoints and "mouth_right" in self.keypoints:
            cv2.circle(img, center=self.keypoints["mouth_left"], radius=1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)
            cv2.circle(img, center=self.keypoints["mouth_right"], radius=1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    def show_nose(self, img):
        if self.keypoints and "nose" in self.keypoints:
            cv2.circle(img, center=self.keypoints["nose"], radius=1, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)

    def show_keypoints(self, img):
        if self.keypoints:
            self.show_eyes(img)
            self.show_mouth(img)
            self.show_nose(img)
    
    def show_confidence(self, img):
        confidence = round(self.confidence*100, 2)
        location = (self.bounding_box["top_left"][0]+self.bounding_box["width"]//2, self.bounding_box["top_left"][1]+self.bounding_box["height"])
        cv2.putText(img, text=f"{confidence}", org=location, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, color=(0, 255, 0), thickness=1, lineType=cv2.LINE_AA)