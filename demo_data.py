from app import db, create_app  # Import your Flask app factory

# Import your models
from app.models.Clubs import Clubs  # Add other models as needed

# Create an app instance
app = create_app()
# Use the app context
with app.app_context():
    # Clear existing data and recreate tables
    db.drop_all()
    db.create_all()

    # Add demo data for Students
    # Add demo data for Clubs
    clubs_data = [
        {
            "name": "Aavartan Dance Club",
            "description": "The official dance club of our college, showcasing various dance forms and organizing performances and workshops.",
            "image": "https://instagram.fjlr3-1.fna.fbcdn.net/v/t51.2885-19/440457092_7459412847505701_5577285138488013095_n.jpg?stp=dst-jpg_tt6&_nc_ht=instagram.fjlr3-1.fna.fbcdn.net&_nc_cat=109&_nc_ohc=f3Nx9hCQSYQQ7kNvgGznH7T&_nc_gid=990cfbc48a544cc7ae7091eff5cdc3ca&edm=AP4sbd4BAAAA&ccb=7-5&oh=00_AYAgHe9rBqb7dLBUiPlXOjKIK95nqEydd09Dzx-VkQXGug&oe=67512A4B&_nc_sid=7a9f4b",
            "type": "Cultural",
            "founded": "2015-01-01",  # Use a standard date format
            "mail": "aavartan@college.edu",
            "coordinator": "23BEC040",
            "co_coordinator": "23BEC035",
            "tags": ["Dance", "Cultural", "Performances", "Workshops"],
        },
        {
            "name": "Samvaad Literary and Quizzing Society",
            "description": "A club for literature enthusiasts and quiz buffs, fostering a love for reading, writing, and competitive quizzing.",
            "image": "https://instagram.fjlr3-1.fna.fbcdn.net/v/t51.2885-19/278629791_317034730383326_8559184586609694117_n.jpg?_nc_ht=instagram.fjlr3-1.fna.fbcdn.net&_nc_cat=102&_nc_ohc=haE8BK0Bk6QQ7kNvgEBxmY0&_nc_gid=e591735a679644338d580012e9d3cc2b&edm=AP4sbd4BAAAA&ccb=7-5&oh=00_AYDUTe0qBOcKTTK4NT7YlxnU0_qgXK6jiSA9ghp4nktiSQ&oe=67513572&_nc_sid=7a9f4b",
            "type": "Literary",
            "founded": "2010-01-01",
            "mail": "samvaad@college.edu",
            "coordinator": "23BEC035",
            "co_coordinator": "23BCS204",
            "tags": ["Literature", "Quizzing", "Debates", "Competitions"],
        },
        {
            "name": "Saaz - The Song Club",
            "description": "The music club of our college, bringing together singers and instrumentalists to create melodious memories.",
            "image": "https://instagram.fjlr3-1.fna.fbcdn.net/v/t51.2885-19/22580109_155154251750578_4546923928852889600_n.jpg?_nc_ht=instagram.fjlr3-1.fna.fbcdn.net&_nc_cat=110&_nc_ohc=gvgolLPuhKwQ7kNvgHlOowH&_nc_gid=07ca2634c5434702a117d4ff29a44022&edm=AP4sbd4BAAAA&ccb=7-5&oh=00_AYA1KZhM8Me6kSArPYWH0ZRjfE4Zx-3aY2e50mhVFF0Uuw&oe=67513E31&_nc_sid=7a9f4b",
            "type": "Cultural",
            "founded": "2012-01-01",
            "mail": "saaz@college.edu",
            "coordinator": "23BCS269",
            "co_coordinator": "23BCS253",
            "tags": ["Music", "Singing", "Instruments", "Cultural Events"],
        },
    ]

    for club in clubs_data:
        new_club = Clubs(
            Name=club["name"],
            Description=club["description"],
            Image=club["image"],
            Type=club["type"],
            Founded=club["founded"],  # Convert to datetime if needed
            Mail=club["mail"],
            Coordinator=club["coordinator"],
            Co_Coordinator=club["co_coordinator"],
            Tags=",".join(club["tags"]),  # Store tags as a comma-separated string
        )
        db.session.add(new_club)

    # Commit the changes
    db.session.commit()

    print("Demo data inserted successfully!")
