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
    
@student_bp.route("/details", methods=["GET"])
def get_student_details():
    rollno = request.args.get("rollno")
    
    if not rollno:
        return jsonify({"error": "RollNo parameter is required"}), 400

    try:
        with db.engine.connect() as conn:
            # Fetch student details
            student_query = text('SELECT * FROM student WHERE student."RollNo" = :rollno')
            student_result = conn.execute(student_query, {"rollno": rollno}).fetchone()

            if not student_result:
                return jsonify({"error": "Student not found"}), 404

            # Convert student details to a dictionary
            student_details = student_result._asdict()

            # Fetch clubs where the student is a member
            club_members_query = text("""
                SELECT clubs.Name FROM club_members 
                JOIN clubs ON club_members.club_name = clubs.Name 
                WHERE club_members.student_id = :rollno
            """)
            club_members_result = conn.execute(club_members_query, {"rollno": rollno}).fetchall()
            member_clubs = [club[0] for club in club_members_result]

            # Fetch clubs where the student is a coordinator
            coordinator_clubs_query = text("""
                SELECT Name FROM clubs 
                WHERE Coordinator = :rollno
            """)
            coordinator_clubs_result = conn.execute(coordinator_clubs_query, {"rollno": rollno}).fetchall()
            coordinator_clubs = [club[0] for club in coordinator_clubs_result]

            # Fetch courses where the student is a CR
            cr_courses_query = text("""
                SELECT Name FROM courses 
                WHERE CR = :rollno
            """)
            cr_courses_result = conn.execute(cr_courses_query, {"rollno": rollno}).fetchall()
            cr_courses = [course[0] for course in cr_courses_result]

        # Prepare the response
        response = {
            "StudentDetails": student_details,
            "Member_Clubs": member_clubs,
            "Coordinator_Clubs": coordinator_clubs,
            "CR_Courses": cr_courses,
        }

        return jsonify(response)
        
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

@student_bp.route("/list", methods=["POST"])
def create_student_api():
    try:
        data = request.get_json()  # Changed from get_data() to get_json()
        if not data or 'id' not in data:
            return jsonify({"error": "Invalid request data"}), 400
            
        with db.engine.connect() as conn:
            query = text("INSERT INTO student VALUES (:id)")
            conn.execute(query, {"id": data['id']})
            conn.commit()  # Add commit to ensure the transaction is saved
            
        return jsonify({"message": "Successfully added student"}), 201
        
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

@student_bp.route("/search", methods=["POST", "GET"])
def search_student():
    name = request.args.get("name")
    rollno = request.args.get("rollno")
    if not name and not rollno:
        return jsonify({"error": "Name or Rollno parameter is required"}), 400

    try:
        query = "SELECT * FROM student WHERE"
        params = {}
        if name:
            query += ' "Name" ILIKE :name'
            params["name"] = f"%{name}%"
        elif rollno:
            query += ' "RollNo" ILIKE :rollno ORDER BY "RollNo"'
            params["rollno"] = f"%{rollno}%"

        with db.engine.connect() as conn:
            result = conn.execute(text(query), params)
            students = [row._asdict() for row in result]

        return jsonify(students)
        
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500