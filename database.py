from sqlalchemy import create_engine, text
import os

db_connection = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    results = conn.execute(text("select * from jobs"))
    jobs = []
    column_names = results.keys()
    for row in results.all():
      jobs.append(dict(zip(column_names, row)))
    return (jobs)


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id={id}"))
    job = []
    column_name = result.keys()
    for rowi in result.all():
      job.append(dict(zip(column_name, rowi)))
    if len(job) == 0:
      return None
    else:
      return (job[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )
    conn.execute(
      query, {
        'job_id': job_id,
        'full_name': data['full_name'],
        'email': data['email'],
        'linkedin_url': data['linkedin_url'],
        'education': data['education'],
        'work_experience': data['work_experience'],
        'resume_url': data['resume_url']
      })
