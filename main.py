from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
  'id': 1,
  'title': 'Front-end developer',
  'location': 'Hyderabad, India',
  'Salary': '10,00,000'
}, {
  'id': 2,
  'title': 'Back-end developer',
  'location': 'Chennai, India',
  'Salary': '20,00,000'
}, {
  'id': 3,
  'title': 'Data Scientist',
  'location': 'Remote',
}, {
  'id': 4,
  'title': 'Data Analyst',
  'location': 'USA',
  'Salary': '$10,000'
}]


@app.route("/")
def hello():
  return render_template('home.html', jobs=jobs, companyname="Current Job")


@app.route("/api/jobs")
def jobs_list():
  return jsonify(jobs)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
