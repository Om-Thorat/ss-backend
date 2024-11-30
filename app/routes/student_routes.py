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
    rollno = request.args.get("rollno")
    if not name and not rollno:
        return jsonify({"error": "Name or Rollno parameter is required"}), 400

    query = "SELECT * FROM student WHERE"
    params = {}
    if name:
        query += ' "Name" ILIKE :name'
        params["name"] = f"%{name}%"
    elif rollno:
        query += ' "RollNo" ILIKE :rollno'
        params["rollno"] = rollno

    with db.engine.connect() as conn:
        result = conn.execute(text(query), params)
        students = [row._asdict() for row in result]

    return jsonify(students)


