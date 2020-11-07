# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template
#create a Flask instance
app = Flask(__name__, template_folder='templates')

#connects default URL of server to a python function
@app.route('/')
@app.route('/home')
def home():
    #function use Flask import (Jinja) to render an HTML template
    return render_template("home.html")

@app.route('/hs_project_plan')
def hs_project_plan():
    return render_template('HelloSeriesPP.html')

@app.route('/hs_project')
def hs_project():
    return render_template('HelloSeriesProject.html')

@app.route('/hs_grading')
def hs_grading():
    return render_template('GradingDocHS.html')

@app.route('/flask_project_plan')
def flask_project_plan():
    return render_template('japanesepp.html')

@app.route('/flask_project')
def flask_project():
    return render_template('JapaneseCultureProject.html')

@app.route('/flask_grading')
def flask_grading():
    return render_template('japanesegradingdoc.html')

@app.route('/week9_videos')
def week9_videos():
    return render_template('week9vids.html')

@app.route('/journals')
def journals():
    return render_template('journals.html')

if __name__ == "__main__":
    #runs the application on the repl development server
    app.run(debug=True)
    #app.run(debug=True, port="5001", host="127.0.0.1")