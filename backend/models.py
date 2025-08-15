from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_path = db.Column(db.String, unique=True, nullable=False)
    file_name = db.Column(db.String, nullable=False)
    date_taken = db.Column(db.DateTime, nullable=True)
    gps_lat = db.Column(db.Float, nullable=True)
    gps_lon = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)