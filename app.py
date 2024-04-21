from flask import Flask, render_template
from jobdata import JOBS

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)

if __name__=="__main__":
    app.run(host="0.0.0.0" , debug=True)