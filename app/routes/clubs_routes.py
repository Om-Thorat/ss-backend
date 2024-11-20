from flask import Blueprint, jsonify, request
from app.models.Clubs import Clubs
from app.models.Student import Student
from app.models.ClubMembers import ClubMembers
from app import db
from sqlalchemy import text

clubs_bp = Blueprint("clubs", __name__, url_prefix="/clubs")


@clubs_bp.route("/list", methods=["GET"])
def get_clubs_api():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM clubs"))
        clubs = [dict(row._mapping) for row in result]
    return jsonify(clubs)


@clubs_bp.route("/list", methods=["POST"])
def create_club_api():
    data = request.get_data()  
    with db.engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO clubs (Name, Type, Founded, Mail, Coordinator, Co_Coordinator) "
                "VALUES (:Name, :Type, :Founded, :Mail, :Coordinator, :Co_Coordinator)"
            ),
            {
                "Name": data["Name"],
                "Type": data["Type"],
                "Founded": data["Founded"],
                "Mail": data["Mail"],
                "Coordinator": data["Coordinator"],
                "Co_Coordinator": data["Co_Coordinator"],
            },
        )
    return "Successfully added club", 201


@clubs_bp.route("/search", methods=["POST"])
def search_club():
    name = request.args.get("name")
    with db.engine.connect() as conn:
        result = conn.execute(
            text('SELECT * FROM clubs WHERE "Name" LIKE :name'), {"name": f"%{name}%"}
        )
        clubs = [dict(row._mapping) for row in result]
    return jsonify(clubs)


@clubs_bp.route("/<name>/members", methods=["GET"])
def get_members_in_club(name):
    with db.engine.connect() as conn:
        result = conn.execute(
            text(
                """
                SELECT s.*
                FROM student s
                INNER JOIN club_members cm ON s.RollNo = cm.student_id
                WHERE cm.club_name = :name
                """
            ),
            {"name": name},
        )
        members = [dict(row._mapping) for row in result]
    return jsonify(members)


@clubs_bp.route("/<name>", methods=["GET"])
def get_club_detail(name):
    with db.engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM clubs WHERE Name = :name"), {"name": name}
        )
        club = [dict(row._mapping) for row in result]
    return jsonify(club[0]) if club else jsonify({"error": "Club not found"}), 404
