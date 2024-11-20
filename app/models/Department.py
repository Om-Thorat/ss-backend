from app import db


class Department(db.Model):
    __tablename__ = "department"
    Name = db.Column(db.String(100), primary_key=True)
    No_of_students = db.Column(db.Integer, nullable=False)
    HOD = db.Column(db.Integer, db.ForeignKey('professor.ID'), nullable=False)

    def __repr__(self):
        return f"<Department {self.Name}>"

    def to_dict(self):
        return {
            "Name": self.Name,
            "No_of_students": self.No_of_students,
            "HOD": self.HOD,
        }
