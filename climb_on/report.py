from climb_on.app import db


class Report(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("user.id"))
    difficulty: str = db.Column(db.String)
    attempts: int = db.Column(db.Integer)
    date: str = db.Column(db.String)
    notes: str = db.Column(db.String)

    def __init__(self, difficulty, attempts, date, notes):
        self.difficulty = difficulty
        self.attempts = attempts
        self.date = date
        self.notes = notes

    def from_form(form: dict[str, str]) -> "Report":
        return Report(
            form.get("difficulty"),
            form.get("attempts"),
            form.get("date"),
            form.get("notes"),
        )
