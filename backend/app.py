from flask import Flask
from database_functions import create_database, init_db

app = Flask(__name__)

init_db(app)

@app.route('/')
def home():
    return "Project A.L.B.U.M Backend is Running"

if __name__ == '__main__':
    create_database(app)
    app.run(debug=True)