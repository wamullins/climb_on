from flask import request, render_template
from climb_on.app import app, db
from climb_on.report import Report


@app.route("/")
def hello_world():
    reports = db.session.execute(db.select(Report).order_by(Report.id)).scalars()
    return render_template("index.html", reports=reports)


@app.route("/", methods=["POST"])
def handle_submission():
    report = Report(
        request.form.get("difficulty"),
        request.form.get("attempts"),
        request.form.get("date"),
        request.form.get("notes"),
    )
    db.session.add(report)
    db.session.commit()

    return hello_world()
