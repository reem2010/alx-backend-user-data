#!/usr/bin/env python3
"""app module
"""
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def route():
    """basic get"""
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
