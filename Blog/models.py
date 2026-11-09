from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')   # lazy parameter is used to increase performance
    comment = db.relationship('Comment', backref='author', lazy='dynamic')   # lazy parameter is used to increase performance

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter_by(email=email).first()
        if user and user.check_password(password):
            access_token = create_access_token(identity=str(user.id))
            return access_token, user

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comment = db.relationship('Comment', lazy='dynamic')

    def to_dict(self):
        return{
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'author_id': self.author_id
        }

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def to_dict(self):
        return{
            'id': self.id,
            'body': self.body,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
            'author_id': self.author_id
        }