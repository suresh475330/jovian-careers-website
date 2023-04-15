from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()


# dbConnectionString = os.getenv("dbString")

engine = create_engine("mysql+pymysql://caza5h15m37220pe6hir:pscale_pw_LmQLDoAduJiPWsPneWxpPaZzwSzUmZL61wIlPcQrEVv@aws.connect.psdb.cloud/makecareers?charset=utf8mb4",connect_args={
    "ssl": {
            "ssl_ca": "/etc/ssl/cert.pem"
        }
})

def getAllJobs():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []

        for row in result.all():
            jobs.append(row._asdict())

        return jobs

def getJobById(id):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT * FROM jobs WHERE id = {id}"))
        job = []

        for row in result.all():
            job.append(row._asdict())

        if len(job) == 0:
            return None
        else:
            return job[0]





def add_application_to_db(job_id, data):
  with engine.connect() as conn:

    full_name=data['full_name'],
    email=data['email'],
    linkedin_url=data['linkedin_url'],
    education=data['education'],
    work_experience=data['work_experience'],
    resume_url=data['resume_url']

    query = text(f"INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ({job_id},'{full_name[0]}','{email[0]}','{linkedin_url[0]}','{education[0]}','{work_experience[0]}','{resume_url}')")
    conn.execute(query)
