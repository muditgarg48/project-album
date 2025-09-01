from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def init_db(app):
    # SQLite DB config
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{app.root_path}/database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

def create_database(app):
    with app.app_context():
        db.create_all() 