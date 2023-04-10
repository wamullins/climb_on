from climb_on.app import db


class Report(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    difficulty: str = db.Column(db.String)
    attempts: int = db.Column(db.Integer)
    date: str = db.Column(db.String)
    notes: str = db.Column(db.String)

    def __init__(self, difficulty, attempts, date, notes):
        self.difficulty = difficulty
        self.attempts = attempts
        self.date = date
        self.notes = notes
