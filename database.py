from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()


dbConnectionString = os.getenv("dbString")

engine = create_engine(dbConnectionString,connect_args={
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
