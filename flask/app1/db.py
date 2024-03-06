from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
import traceback
from urllib.parse import quote
password=quote('cHARIZOD100@')
db_uri=f"mysql://root:{password}@localhost/avisoft"

# In URLs, certain characters have special meanings, such as @ being used to separate the username and password from the hostname. 
# Therefore, if your password contains these special characters, you need to percent-encode them.
# In Python, you can use the quote() function from the urllib.parse module to encode the password. Here's how you can do it

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    title=db.Column(db.String(250),nullable=False)
    location=db.Column(db.String(250),nullable=False)
    requirements=db.Column(db.String(2000))
    responsibilities=db.Column(db.String(2000))
    salary=db.Column(db.Integer)
    currency=db.Column(db.String(10))
    # Define other columns as needed

def load_jobs_from_db():
    try:
        jobs = Job.query.all()  # Query all jobs from the database
        job_dicts = []  # Create an empty list to store dictionaries representing jobs
        for job in jobs:  # Iterate over each job object returned by the query
            job_dict = {}  # Create an empty dictionary to represent the current job
            for column in job.__table__.columns:  # Iterate over each column in the job table
                # Populate the job dictionary with column name and value
                job_dict[column.name] = getattr(job, column.name)
            job_dicts.append(job_dict)  # Add the job dictionary to the list
        return job_dicts  # Return the list of job dictionaries
    except Exception as e:
        # Error handling: Print the error message and return an empty list
        print("An error occurred while retrieving data from the database:")
        print(traceback.format_exc())  # Print the traceback for debugging purposes
        return []

from flask import jsonify

@app.route('/jobs')
def get_jobs():
    jobs = load_jobs_from_db()
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(debug=True)