from flask import Blueprint, jsonify, request
from app.models.Courses import Courses
from app.models.Student import Student
from app.models.StudentCourses import StudentCourses
from app import db
from sqlalchemy import text


courses_bp = Blueprint("courses", __name__, url_prefix="/courses")


@courses_bp.route("/list", methods=["GET"])
def get_courses_api():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM courses"))
        courses = [dict(row._mapping) for row in result]
    return jsonify(courses)


@courses_bp.route("/list", methods=["POST"])
def create_course_api():
    data = request.get_data()  
    with db.engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO courses (Code, Name, Lab, Duration, Credit, Elective, CR, Department) "
                "VALUES (:Code, :Name, :Lab, :Duration, :Credit, :Elective, :CR, :Department)"
            ),
            {
                "Code": data["Code"],
                "Name": data["Name"],
                "Lab": data["Lab"],
                "Duration": data["Duration"],
                "Credit": data["Credit"],
                "Elective": data["Elective"],
                "CR": data["CR"],
                "Department": data["Department"],
            },
        )
    return "Successfully added course", 201


@courses_bp.route("/search", methods=["POST"])
def search_course():
    name = request.args.get("name")
    with db.engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM courses WHERE "Name" LIKE :name'), {"name": f"%{name}%"}
        )
        courses = [dict(row._mapping) for row in result]
    return jsonify(courses)

# Retrieves all students enrolled in a course
@courses_bp.route("/<code>/students", methods=["GET"])
def get_students_in_course(code):
    with db.engine.connect() as conn:
        result = conn.execute(
            text(
                """
                SELECT s.* 
                FROM student s
                INNER JOIN student_courses sc ON s.RollNo = sc.student_id
                WHERE sc.course_code = :code
                """
            ),
            {"code": code},
        )
        students = [dict(row._mapping) for row in result]
    return jsonify(students)


@courses_bp.route("/<code>", methods=["GET"])
def get_course_detail(code):
    with db.engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM courses WHERE Code = :code"), {"code": code}
        )
        course = [dict(row._mapping) for row in result]
    return jsonify(course[0]) if course else jsonify({"error": "Course not found"}), 404

#Searches for students by name enrolled in a specific course.
@courses_bp.route("/<code>/search-student", methods=["POST"])
def search_student_in_course(code):
    name = request.args.get("name")
    with db.engine.connect() as conn:
        result = conn.execute(
            text(
                """
                SELECT s.*
                FROM student s
                INNER JOIN student_courses sc ON s.RollNo = sc.student_id
                WHERE sc.course_code = :code AND s.Name LIKE :name
                """
            ),
            {"code": code, "name": f"%{name}%"},
        )
        students = [dict(row._mapping) for row in result]
    return jsonify(students)
