from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from sqlalchemy import text

from app import db
from app.models.Student import Student

student_bp = Blueprint("student", __name__, url_prefix="/student")


@student_bp.route("/list", methods=["GET"])
def get_students_api():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM student"))
        students = [row._asdict() for row in result]
    return jsonify(students)


@student_bp.route("/list", methods=["POST"])
def create_student_api():
    data = request.get_data()
    print(data)
    with db.engine.connect() as conn:
        conn.execute(text(f"INSERT INTO student VALUES ('{data['id']}')"))
    return "Sucessfully added student", 201


@student_bp.route("/search", methods=["POST", "GET"])
def search_student():
    name = request.args.get("name")
    if not name:
        return jsonify({"error": "Name parameter is required"}), 400

    query = text('SELECT * FROM student WHERE "Name" ILIKE :name')
    with db.engine.connect() as conn:
        result = conn.execute(query, {"name": f"%{name}%"})
        students = [row._asdict() for row in result]

    return jsonify(students)
