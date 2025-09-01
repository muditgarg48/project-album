from database_functions import db

class MediaDeviceOrigin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String, nullable=True)
    model = db.Column(db.String, nullable=True)
    software = db.Column(db.String, nullable=True)
    exif_version = db.Column(db.String, nullable=True)

class MediaProperties(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Integer, nullable=True)
    height = db.Column(db.Integer, nullable=True)
    properties = db.Column(db.JSON, nullable=True)

class MediaLocation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    altitude = db.Column(db.Float, nullable=True)

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String, unique=True, nullable=False)
    file_size = db.Column(db.Integer, nullable=True)
    date_timestamp = db.Column(db.DateTime, nullable=True)
    orientation = db.Column(db.Integer, nullable=True)
    file_origin = db.relationship('MediaDeviceOrigin', backref='image', uselist=False)
    location = db.relationship('MediaLocation', backref='image', uselist=False)
    properties = db.relationship('MediaProperties', backref='image', uselist=False)