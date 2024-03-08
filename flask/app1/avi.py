from flask import Flask, render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy
import os
import traceback
from urllib.parse import quote
from sqlalchemy.exc import SQLAlchemyError


password = quote('cHARIZOD100@')
db_uri = f"mysql://root:{password}@localhost/avisoft"

app1 = Flask(__name__)
app1.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app1.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app1)  # Initialize SQLAlchemy with the Flask app instance

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    requirements = db.Column(db.String(2000))
    responsibilities = db.Column(db.String(2000))
    salary = db.Column(db.Integer)
    currency = db.Column(db.String(10))
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
    except SQLAlchemyError as e:
        # Error handling: Print the error message and return an empty list
        print("An error occurred while retrieving data from the database:",e)
        print(traceback.format_exc())  # Print the traceback for debugging purposes
        return []

def load_specific_job(job_id):
    job=Job.query.get(job_id)
    if job:
        job_dict={
            'id':job.id,
            'title':job.title,
            'location':job.location,
            'requirements':job.requirements,
            'responsibilities':job.responsibilities,
            'salary':job.salary,
            'currency':job.currency
        }
        return job_dict
    else:
        return None

@app1.route("/")  # routing or setting the url
def avi():
    jobs=load_jobs_from_db()
    return render_template("home2.html",jobs=jobs)    

@app1.route("/api/jobs")  # api endpoint
def list_jobs():
    jobs=load_jobs_from_db()
    return jsonify(jobs)# jsonify convert the data in json data like an api

@app1.route("/job/<int:id>")
def show_job(id):
    job=load_specific_job(id)
    if job is None:
        return jsonify({"error":"Job not found"}),404
    return render_template('jobpage.html',job=job)


# creating the instance od the table with corresponding fields
class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    job_id = db.Column(db.Integer, nullable=False)
    full_name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    linkedin_url = db.Column(db.String(500))
    education = db.Column(db.String(2000))
    work_experience = db.Column(db.String(2000))
    resume_url = db.Column(db.String(500))

def add_application_to_db(job_id, data):
    try:
        # Create a new Application object
        application = Application(
            job_id=job_id,
            full_name=data['full_name'],
            email=data['email'],
            linkedin_url=data['linkedin_url'],
            education=data['education'],
            work_experience=data['work_experience'],
            resume_url=data['resume_url']
        )

        db.session.add(application) # here session is used to manage a particular database and used to add,delete,update the database

        db.session.commit()  # commit the transaction to save the application to the databse
    except SQLAlchemyError as e:
        db.session.rollback()  # rollback the trasaction in cas of the error
        print(f"Error adding application to database : {e}")

    except KeyError as e:
        db.session.rollback()
        print(f"Error adding application to database: Required field '{e.args[0]}' is missing.")
        return False  # Return False to indicate failure
        
@app1.route("/job/<int:id>/apply",methods=['post'])
def apply_to_job(id):
    # data=request.args get the data from the url
    data=request.form
    add_application_to_db(id,data)
    return render_template('application_submit.html',application=data)