from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class Device(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    deviceId = db.Column(db.String(64), index=True, unique=True)
    devicename = db.Column(db.String(128))
    name = db.Column(db.String(128))
    dept_code = db.Column(db.String(128))
    device_function = db.Column(db.String(128))
    device_bg = db.Column(db.String(128))

    # device_image = # HAVE TO LET USER UPLOAD IMAGE OF THE DEVICE
    # background_img = # HAVE TO LET USER SELECT WHICH IMAGE TO USE AS BACKGROUND FROM DROPDOWN LIST

    def __repr__(self):
        return '<Device Id:{}>'.format(self.deviceId)
    # def __repr__(self): # FOR DEBUG
    #     return '''<Device Name:{}> \n<Device Id:{}> \n<Name:{}> 
    #     \n<Dept.Code:{}> \n<Device Function:{}>'''.format(self.devicename, 
    #     self.deviceId, self.name, self.dept_code, self.device_function)

# db.create_all()
# db.session.commit()