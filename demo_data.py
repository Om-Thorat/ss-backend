from app import db, create_app  # Import your Flask app factory

# Import your models
from app.models import (
    Student,
    # Guardian,
    # Clubs,
    # Member,
    # Courses,
    # Hostel,
    # Department,
    # Programme,
    # Professor,
)

# Create an app instance
app = create_app()

# Use the app context
with app.app_context():
    # Clear existing data and recreate tables
    db.drop_all()
    db.create_all()

    # Add demo data
    # Add Students
    student1 = Student.Student(
        RollNo=1,
        Name="John Doe",
        Branch="Computer Science",
        DOB="2000-05-15",
        Phone="1234567890",
        Hometown="Springfield",
        BloodGroup="O+",
    )
    student2 = Student.Student(
        RollNo=2,
        Name="Jane Smith",
        Branch="Electrical Engineering",
        DOB="1999-09-20",
        Phone="0987654321",
        Hometown="Shelbyville",
        BloodGroup="A+",
    )
    db.session.add_all([student1, student2])

    # # Add Guardians
    # guardian1 = Guardian(
    #     Name="Mary Doe", Hometown="Springfield", Relation="Mother", StudentRollNo=1
    # )
    # guardian2 = Guardian(
    #     Name="Mark Smith", Hometown="Shelbyville", Relation="Father", StudentRollNo=2
    # )
    # db.session.add_all([guardian1, guardian2])

    # # Add Clubs
    # club1 = Clubs(
    #     Name="Coding Club",
    #     Type="Technical",
    #     Founded="2018-03-10",
    #     Mail="codingclub@example.com",
    #     Coordinator=1,
    #     Co_Coordinator=2,
    # )
    # club2 = Clubs(
    #     Name="Robotics Club",
    #     Type="Technical",
    #     Founded="2017-07-15",
    #     Mail="roboticsclub@example.com",
    #     Coordinator=2,
    #     Co_Coordinator=1,
    # )
    # db.session.add_all([club1, club2])

    # # Add other models similarly...
    # # Add Members, Courses, Hostels, Departments, Programmes, Professors here as in the earlier example

    # # Commit the changes
    db.session.commit()

    print("Demo data inserted successfully!")
