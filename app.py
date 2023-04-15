from flask import Flask, render_template, jsonify, request
from database import getAllJobs, getJobById, add_application_to_db
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
from flask_hcaptcha import hCaptcha

load_dotenv()

app = Flask(__name__)

# flask_mail config
app.config['MAIL_SERVER']= "smtp.gmail.com"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
# HCaptcha config
app.config['HCAPTCHA_ENABLED'] = True
app.config['HCAPTCHA_SITE_KEY'] = os.getenv('HCAPTCHA_SITE_KEY')
app.config['HCAPTCHA_SECRET_KEY'] = os.getenv('HCAPTCHA_SECRET_KEY')

mail = Mail(app)
hcaptcha = hCaptcha(app)

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


def sendMailToAdmin(name,jobTitle):
    mailMsg = Message(
        "Job application from Make Careers",
        sender='skdeveloper10@gmail.com',
        recipients=['skdeveloper10@gmail.com'])
    mailMsg.body = f"You have a new client {name}. he/she was application for the role of {jobTitle} at Make Careers. Plz check out the database for more informations"
    mail.send(mailMsg)

def sendMailToClient(email,name,jobTitle):
    mailMsg = Message(
        "Application submission from Make Careers",
        sender='skdeveloper10@gmail.com',
        recipients=[email])
    mailMsg.body = f"Hi {name} Your application for the role of {jobTitle} at Make Careers has been submitted successfully!"
    mail.send(mailMsg)


@app.route("/job/<id>/apply", methods=['POST'])
def applyToJob(id):
    data = request.form
    job = getJobById(id)

    if hcaptcha.verify():
        add_application_to_db(id,data)
        sendMailToAdmin(data['full_name'],job['title'])
        sendMailToClient(data['email'],data['full_name'],job['title'])
        return render_template('applicationReview.html',  application=data, job=job)
    else:
        return render_template("jobPage.html",job=job,hCaptchaError="hCaptcha not verify")

# API Routes

@app.route("/api/jobs")
def allJobList():
    jobs = getAllJobs()
    return jsonify(jobs)

@app.route("/api/job/<id>")
def singleJobList(id):
    job = getJobById(id)
    return jsonify(job)
