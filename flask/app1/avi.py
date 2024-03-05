from flask import Flask,render_template,jsonify

app1=Flask(__name__)  # creating an object of Flask

JOBS=[
    {
        'id':1,
        'title':'Data Analyst',
        'location':'Bengaluru,India',
        'salary':'Rs 1,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Delhi,India',
        'salary':'Rs 15,00,000'
    },
    {
        'id':3,
        'title':'frontend Engineer',
        'location':'Remote',
        'salary':'Rs 12,00,000'
    },
    {
        'id':4,
        'title':'Backend Engineer',
        'location':'Mohali, India',
        'salary':'Rs 14,00,000'
    }
]

@app1.route("/")  # routing or setting the url
def avi():
    return render_template("home2.html",jobs=JOBS)    

@app1.route("/api/jobs")  # api endpoint
def list_jobs():
    return jsonify(JOBS)  # jsonify convert the data in json data like an api

