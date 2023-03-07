from flask import Flask,request,render_template

app = Flask(__name__)

reports=[]

@app.route("/")
def hello_world():
    return render_template("index.html", reports=reports)

@app.route("/",methods=["POST"])
def handle_submission():
    for key in request.form.keys():
        print(request.form.get(key))
    reports.append(request.form.to_dict())
    return hello_world()