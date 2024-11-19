from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app.models.users import Users
from app import db
from sqlalchemy import text

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/api/list', methods=['GET'])
def get_users_api():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        users = [str(row) for row in result]
    return jsonify(users)

@user_bp.route('/api/list', methods=['POST'])
def create_user_api():
    data = request.get_data()
    print(data)
    with db.engine.connect() as conn:
        conn.execute(text(f"INSERT INTO users VALUES ('{data['id']}')"))
    return "Sucessfully added user", 201