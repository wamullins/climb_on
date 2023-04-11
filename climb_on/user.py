from climb_on.app import db


class User(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String)
    name: str = db.Column(db.String)
    password: str = db.Column(db.String)
    reports = db.relationship("Report", backref="user", lazy=True)
