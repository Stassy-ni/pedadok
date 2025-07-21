from extentions import db
from uuid import uuid4

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.String(), primary_key=True, default=str(uuid4()))
    usersurname = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Text(), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'