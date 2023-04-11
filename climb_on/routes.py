from flask import request, render_template
from climb_on.app import app, db
from climb_on.report import Report
from climb_on.user import User


@app.route("/<int:user_id>", methods=["GET", "POST"])
def report_view(user_id: int):
    if request.method == "POST":
        report = Report.from_form(request.form)
        db.session.add(report)
        db.session.commit()

    user = User.query.get(user_id)

    return render_template("index.html", reports=user.reports)
