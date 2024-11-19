from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.String(60), primary_key=True)

    def __repr__(self):
        return f'<User {self.id}>'

    def to_dict(self):
        return {
            'id': self.id
        }
