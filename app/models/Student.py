from app import db
from datetime import datetime

class Student(db.Model):
    __tablename__ = "student"
    RollNo = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Branch = db.Column(db.String(100))
    DOB = db.Column(db.Date)
    Phone = db.Column(db.String(15))
    Hometown = db.Column(db.String(100))
    BloodGroup = db.Column(db.String(5))

    StudentCourses = db.relationship("StudentCourses", backref="student", lazy=True)

    def __repr__(self):
        return f"<Student {self.Name}>"

    def to_dict(self):
        return {
            "RollNo": self.RollNo,
            "Name": self.Name,
            "Branch": self.Branch,
            "DOB": self.DOB,
            "Phone": self.Phone,
            "Hometown": self.Hometown,
            "BloodGroup": self.BloodGroup,
        }
