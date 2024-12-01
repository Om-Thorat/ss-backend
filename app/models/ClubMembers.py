from app import db



class ClubMembers(db.Model):
    __tablename__ = "club_members"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    club_name = db.Column(db.String(100), db.ForeignKey("clubs.Name"), nullable=False)
    student_id = db.Column(db.String(15), db.ForeignKey("student.RollNo"), nullable=False)

    def __repr__(self):
        return f"<ClubMembers Club={self.club_name}, Student={self.student_id}>"

    def to_dict(self):
        return {
            "id": self.id,
            "club_name": self.club_name,
            "student_id": self.student_id,
        }


