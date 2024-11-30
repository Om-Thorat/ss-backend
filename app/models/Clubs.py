from app import db


class Clubs(db.Model):
    __tablename__ = "clubs"
    Name = db.Column(db.String(100), primary_key=True)
    Website = db.Column(db.String(255), nullable=True)
    Email = db.Column(db.String(100), unique=True, nullable=False)
    Counselor_Name = db.Column(db.String(100), nullable=False)
    Counselor_Phone = db.Column(db.String(15), nullable=False)
    Counselor_Email = db.Column(db.String(100), unique=True, nullable=False)
    Coordinator = db.Column(db.String(15), db.ForeignKey("student.RollNo", ondelete="RESTRICT"), nullable=False)

    Members = db.relationship("ClubMembers", backref="club", lazy=True)

    def __repr__(self):
        return f"<Club {self.Name}>"

    def to_dict(self):
        return {
            "Name": self.Name,
            "Website": self.Website,
            "Email": self.Email,
            "Counselor_Name": self.Counselor_Name,
            "Counselor_Phone": self.Counselor_Phone,
            "Counselor_Email": self.Counselor_Email,
            "Coordinator": self.Coordinator,
        }
