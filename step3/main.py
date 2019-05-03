import os
from flask import Flask

SECRET_KEY = os.getenv("SECRET_KEY")
MESSAGE = os.getenv("MESSAGE", "Hello from microservice!")

app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/', methods=['GET'])
def index():
    return MESSAGE


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
