from flask import Flask, render_template, jsonify
from database import getAllJobs 

app = Flask(__name__)

@app.route("/")
def home():
    jobs = getAllJobs()
    return render_template("home.html", jobs=jobs, companyName="Make Careers")

@app.route("/api/jobs")
def jobList():
    jobs = getAllJobs()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)
