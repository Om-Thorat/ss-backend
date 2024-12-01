from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from sqlalchemy import text

from app import db

login_bp = Blueprint("user", __name__, url_prefix="/user")


@login_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data["username"]
    password = data["password"]
    print(username, password)
    query = text(
        'SELECT * FROM login WHERE "roll" = :username AND "password" = :password'
    )
    with db.engine.connect() as conn:
        result = conn.execute(query, {"username": username, "password": password})
        user = [row._asdict() for row in result]
    if len(user):
        user[0]["token"] = hash(user[0]["password"] + user[0]["roll"])
    print(user)
    return (
        jsonify(user) if user else jsonify({"error": "Invalid username or password"})
    ), 200
