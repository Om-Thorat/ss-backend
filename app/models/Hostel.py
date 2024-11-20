from app import db


class Hostel(db.Model):
    __tablename__ = "hostel"
    Name = db.Column(db.String(100), primary_key=True)
    No_of_rooms = db.Column(db.Integer, nullable=False)
    Warden = db.Column(db.Integer, db.ForeignKey("professor.ID"), nullable=False)

    Students = db.relationship("Student", backref="hostel", lazy=True)

    def __repr__(self):
        return f"<Hostel {self.Name}>"

    def to_dict(self):
        return {
            "Name": self.Name,
            "No_of_rooms": self.No_of_rooms,
            "Warden": self.Warden,
            "Students": [student.RollNo for student in self.Students],
        }
