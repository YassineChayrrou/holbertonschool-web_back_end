#!/usr/bin/env python3
""" Flask app module """


from flask import Flask, jsonify, request
from auth import Auth


app = Flask(__name__)
auth = Auth()


@app.route("/", methods=['GET'])
def index():
    return jsonify({"message": "Bienvenue"})


@app.route("/users", methods=['POST'])
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = auth.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"})
    return jsonify({
        "email": email,
        "message": "user created"
        })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
