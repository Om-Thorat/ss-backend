from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app.models.Student import Student
from app import db
from sqlalchemy import text

student_bp = Blueprint("student", __name__, url_prefix="/student")


@student_bp.route("/list", methods=["GET"])
def get_students_api():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM student"))
        students = [str(row) for row in result]
    return jsonify(students)


@student_bp.route("/list", methods=["POST"])
def create_student_api():
    data = request.get_data()
    print(data)
    with db.engine.connect() as conn:
        conn.execute(text(f"INSERT INTO student VALUES ('{data['id']}')"))
    return "Sucessfully added student", 201


@student_bp.route("/search", methods=["POST"])
def search_student():
    print(request.args)
    name = request.args.get("name")
    with db.engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM student WHERE "Name" LIKE :name'), {"name": f"%{name}%"}
        )
        student = [dict(row._mapping) for row in result]
    return jsonify(student)
