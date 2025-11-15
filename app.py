from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id' : 1,
        'title' : 'Data Analyst',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 10,00,000'
    },

     {
        'id' : 2,
        'title' : 'Data Scientist',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 15,00,000'
    },

     {
        'id' : 3,
        'title' : 'Software Engineer',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 10,00,000'
    },

     {
        'id' : 4,
        'title' : 'software developer',
        'location' : 'Delhi, India',
    },

     {
        'id' : 5,
        'title' : 'Frontend Engineer',
        'location' : 'Delhi, India',
        'salary' : 'Rs. 19,00,000'
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)