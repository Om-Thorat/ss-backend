from app import db


class Courses(db.Model):
    __tablename__ = "courses"
    Code = db.Column(db.String(10), primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Lab = db.Column(db.Boolean, default=False)
    Duration = db.Column(db.Integer, nullable=False)
    Credit = db.Column(db.Integer, nullable=False)
    Elective = db.Column(db.Boolean, default=False)
    CR = db.Column(db.Integer, db.ForeignKey('student.RollNo'), nullable=False)
    Department = db.Column(db.String(100), db.ForeignKey('department.Name'), nullable=False)

    def __repr__(self):
        return f"<Courses {self.Name}>"

    def to_dict(self):
        return {
            "Code": self.Code,
            "Name": self.Name,
            "Lab": self.Lab,
            "Duration": self.Duration,
            "Credit": self.Credit,
            "Elective": self.Elective,
            "CR": self.CR,
            "Department": self.Department,
        }
