from app import db

class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(100))
    zipcode = db.Column(db.Integer)
    projects = db.relationship('Project', backref='account')