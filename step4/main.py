import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
SECRET_KEY = os.getenv("SECRET_KEY")
DB_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MESSAGE = os.getenv("MESSAGE", "Hello from microservice!")

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{DB_PASSWORD}@db/mysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class WorkshopUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/', methods=['GET'])
def index():
    return MESSAGE


@app.route('/user', methods=['GET'])
def list_users():
    users = WorkshopUser.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    try:
        user = WorkshopUser(data["username"], data["email"])
        db.session.add(user)
        db.session.commit()
        return jsonify({"user": user.id})
    except IntegrityError:
        return jsonify({"user": "error"}), 422


if __name__ == "__main__": 
    db.create_all()
    app.run(host="0.0.0.0", port=5000, debug=True)
