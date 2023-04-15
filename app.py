from distutils.file_util import write_file
from flask import Flask, render_template, request, session
from calculator import Calculator


app = Flask(__name__)
calculator = Calculator()

@app.route("/")
def homePage():
   name = 'Group 8\'s Calculator'
   return render_template('ui.html')


if __name__ == "main":
   app.run(debug=True)