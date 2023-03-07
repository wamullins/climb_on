from flask import Flask,request

app = Flask(__name__)

reports=[]

@app.route("/")
def hello_world():
    rendered_reports=""
    for report in reports:
        rendered_reports+=f"""<div>{report["difficulty"]}: {report["attempts"]}: {report["date"]}: {report["notes"]}</div>"""
    return """<div>
    <h1>Climb On!</h1>
    <form method="post">
        <div>
            <label>Difficulty</label>
            <input name="difficulty"/>
        </div>
        <div>
            <label>Number of Attempts</label>
            <input name="attempts"/>
        </div>
        <div>
            <label>Date Completed</label>
            <input name="date"/>
        </div>
        <div>
            <label>Notes</label>
            <textarea name="notes"></textarea>
        </div>
        <button>Send it</button>
    </form>"""+rendered_reports+"""</div>"""

@app.route("/",methods=["POST"])
def handle_submission():
    for key in request.form.keys():
        print(request.form.get(key))
    reports.append(request.form.to_dict())
    return hello_world()