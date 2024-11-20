from app import db


class Professor(db.Model):
    __tablename__ = "professor"
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(15))
    Designation = db.Column(db.String(100))
    Mail = db.Column(db.String(100), unique=True, nullable=False)
    DepartmentName = db.Column(db.String(100), db.ForeignKey('department.Name'), nullable=False)

    def __repr__(self):
        return f"<Professor {self.Name}>"

    def to_dict(self):
        return {
            "ID": self.ID,
            "Name": self.Name,
            "Phone": self.Phone,
            "Designation": self.Designation,
            "Mail": self.Mail,
            "DepartmentName": self.DepartmentName,
        }
