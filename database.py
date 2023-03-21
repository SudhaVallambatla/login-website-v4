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
    jobss = []
    column_names = results.keys()
    for row in results.all():
      jobss.append(dict(zip(column_names, row)))
    return (jobss)
