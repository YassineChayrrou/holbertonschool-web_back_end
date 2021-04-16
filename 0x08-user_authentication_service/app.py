#!/usr/bin/env python3
""" Flask app module """


from flask import Flask
from flask import jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
