from app import db
from datetime import datetime

class StudentCourses(db.Model):
    __tablename__ = "student_courses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.RollNo"), nullable=False)
    course_code = db.Column(db.String(10), db.ForeignKey("courses.Code"), nullable=False)

    def __repr__(self):
        return f"<StudentCourses StudentID={self.student_id}, CourseCode={self.course_code}>"

    def to_dict(self):
        return {
            "id": self.id,
            "student_id": self.student_id,
            "course_code": self.course_code,
        }
