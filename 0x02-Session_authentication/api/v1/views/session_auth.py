#!/usr/bin/env python3
""" Module of session views
"""
from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """login method"""
    password = request.form.get('password')
    email = request.form.get('email')
    if (not(email) or email == ""):
        return jsonify({"error": "email missing"}), 400
    if (not(password) or password == ""):
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({"email": email})
        if(len(user) == 0):
            return jsonify({"error": "no user found for this email"}), 404
        user = user[0]
        if (not(user.is_valid_password(password))):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        out = jsonify(user.to_json())
        key = os.getenv('SESSION_NAME')
        out.set_cookie(key, session_id)
        return out
    except Exception as err:
        return jsonify({"error": "no user found for this email"}), 404
