#!/usr/bin/env python3
"""app module
"""
from flask import Flask, jsonify, request, abort, redirect
from auth import Auth


AUTH = Auth()


app = Flask(__name__)


@app.route("/")
def route():
    """basic get"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """register a user"""
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify({"email": email, "message": "user created"})
    except Exception as e:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """login endpoint"""
    email = request.form.get('email')
    password = request.form.get('password')
    if(not(AUTH.valid_login(email, password))):
        abort(401)
    session_id = AUTH.create_session(email)
    res = jsonify({"email": email, "message": "logged in"})
    res.set_cookie('session_id', session_id)
    return res


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """logout"""
    session = request.cookies.get('session_id')
    if (not session):
        abort(403)
    user = AUTH.get_user_from_session_id(session)
    if user:
        redirect('/')
    else:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
