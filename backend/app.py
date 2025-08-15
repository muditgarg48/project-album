from flask import Flask
from models import db, Image

app = Flask(__name__)

# SQLite DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Project A.L.B.U.M Backend is Running"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)