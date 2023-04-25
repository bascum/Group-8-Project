from distutils.file_util import write_file
from flask import Flask, render_template, request
from calculator import Calculator


app = Flask(__name__)
app.secret_key = "my_secretKey"
calculator = Calculator()


typed = ""
wholeOp = ""

@app.route("/", methods=['GET', 'POST'])
def homePage():
   
   global typed
   global wholeOp
   
   if request.method == "POST":
      # Get the button that was clicked
         button = request.form["button"]
         # Update the display screen based on the button clicked
         if button == "AC":
            wholeOp = ""
            typed = ""
            
         elif button == "CH":
            calculator.clearHist()
            
         elif button in "123456789":
            typed += button
            
         elif button == ".":
            if typed in "123456789":
               typed += "."
               
         elif button == "0":
            if typed == "":
               pass
            else:
               typed = typed + "0"
               
         elif button == "negate":
            if typed[0] == "-":
               del typed[0]
            else:
               typed = "-" + typed
               
         elif button == "div":
            if typed == "":
               pass
            else:
               wholeOp = wholeOp + typed + " / "
               typed = ""
               
         elif button == "mul":
            if typed == "":
               pass
            else:
               wholeOp = wholeOp + typed + " * "
               typed = ""
               
         elif button == "sub":
            if typed == "":
               pass
            else:
               wholeOp = wholeOp + typed + " - "
               typed = ""
               
         elif button == "add":
            if typed == "":
               pass
            else:
               wholeOp = wholeOp + typed + " + "
               typed = ""
               
         elif button == "back":
            if typed == "":
               pass
            else:
               typed = typed[:-1]
               
         elif button == "equ":
            if typed == "" and wholeOp == "":
               pass
            elif wholeOp == "":
               pass
            else:
               calculator.calculate(wholeOp + typed)
               wholeOp = ""
               typed = ""
               
   return render_template('ui.html', wholeOp=wholeOp, typed=typed, history=calculator.getHist())


if __name__ == "__main__":
   app.run(debug=True)