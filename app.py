from flask import Flask, render_template, jsonify
from database import getAllJobs, getJobById

app = Flask(__name__)

@app.route("/")
def home():
    jobs = getAllJobs()
    return render_template("home.html", jobs=jobs)

@app.route("/job/<id>")
def showJob(id):
    job = getJobById(id)
    if not job:
        return "Not Found", 404
    return render_template("jobPage.html",job=job)


@app.route("/api/jobs")
def allJobList():
    jobs = getAllJobs()
    return jsonify(jobs)

@app.route("/api/job/<id>")
def singleJobList(id):
    job = getJobById(id)
    return jsonify(job)

if __name__ == "__main__":
    app.run(debug=True)
