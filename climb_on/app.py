from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql://postgres:mysecretpassword@localhost:5432/default"
db.init_app(app)

with app.app_context():
    db.create_all()

import climb_on.routes
