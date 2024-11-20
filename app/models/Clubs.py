from app import db



class Clubs(db.Model):
    __tablename__ = "clubs"
    Name = db.Column(db.String(100), primary_key=True)
    Type = db.Column(db.String(50), nullable=False)
    Founded = db.Column(db.Date, nullable=False)
    Mail = db.Column(db.String(100), unique=True, nullable=False)
    Coordinator = db.Column(db.Integer, db.ForeignKey("student.RollNo"), nullable=False)
    Co_Coordinator = db.Column(db.Integer, db.ForeignKey("student.RollNo"), nullable=True)

    Members = db.relationship("ClubMembers", backref="club", lazy=True)

    def __repr__(self):
        return f"<Club {self.Name}>"

    def to_dict(self):
        return {
            "Name": self.Name,
            "Type": self.Type,
            "Founded": self.Founded,
            "Mail": self.Mail,
            "Coordinator": self.Coordinator,
            "Co_Coordinator": self.Co_Coordinator,
        }
