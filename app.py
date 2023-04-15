from distutils.file_util import write_file
from flask import Flask, render_template, request, session


app = Flask(__name__)

# def readDetails(filename):
#    with open(filename, 'r') as f:
#       return [line for line in f]


@app.route("/")
def homePage():
   name = 'Group 8\'s Calculator'
   #details = ['This is my name', 'I am from earth'] #<- instead of this we'll use a function
#    details = readDetails('static\details.txt')
   return render_template('ui.html')

# @app.route('/form', methods=['GET', 'POST'])
# def formDemo():
#    quote = None
#    if request.method == 'POST':
#       quote = request.form['nm']
#    #ends with the above at 36:35 on panopto
#    # if request.form['message']:
#    #    write_file('Wk10\personalSiteApp\static\quotes.txt', request.form['quote'])

#    return render_template('form.html', quote=quote)



if __name__ == "main":
    app.run(debug = True)
