

from app import db, create_app  # Import your Flask app factory

# Import your models
from app.models.ClubMembers import ClubMembers  # Import ClubMembers model

# Create an app instance
app = create_app()
# Use the app context
with app.app_context():
    # Clear existing data and recreate tables
    db.drop_all()
    db.create_all()

    club_members_data = [
        # Members for "Aavartan Dance Club"
        {"club_name": "Aavartan Dance Club", "student_id": "23BCS214"},
        {"club_name": "Aavartan Dance Club", "student_id": "23BCS105"},
        {"club_name": "Aavartan Dance Club", "student_id": "23BCS141"},
        # Members for "Samvaad Literary and Quizzing Society"
        {"club_name": "Samvaad Literary and Quizzing Society", "student_id": "23BCS111"},
        {"club_name": "Samvaad Literary and Quizzing Society", "student_id": "23BCS179"},
        {"club_name": "Samvaad Literary and Quizzing Society", "student_id": "23BCS143"},
        # Members for "Saaz - The Song Club"
        {"club_name": "Saaz - The Song Club", "student_id": "23BCS214"},
        {"club_name": "Saaz - The Song Club", "student_id": "23BCS093"},
        {"club_name": "Saaz - The Song Club", "student_id": "23BCS116"},
    ]

    for member in club_members_data:
        new_member = ClubMembers(
            club_name=member["club_name"],
            student_id=member["student_id"]
        )
        db.session.add(new_member)

    # Commit the changes
    db.session.commit()

    print("ClubMembers demo data inserted successfully!")
