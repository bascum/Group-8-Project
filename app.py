from distutils.file_util import write_file
from flask import Flask, render_template, request, session
from calculator import Calculator


app = Flask(__name__)
app.secret_key = "my_secretKey"
calculator = Calculator()


typed = ""
wholeOp = ""
modFlag = False

if modFlag == True:
   wholeOp = wholeOp + typed
   wholeOp = calculator.calculate(wholeOp)

@app.route("/", methods=['GET', 'POST'])
def homePage():
   
   global typed
   global wholeOp
   global modFlag
   
   if request.method == "POST":
      # Get the button that was clicked
         button = request.form["button"]
         # Update the display screen based on the button clicked
         if button == "AC":
            wholeOp = ""
            typed = ""
            count = 0
         elif button == "1":
            typed = typed + "1"
         elif button == "2":
            typed = typed + "2"
         elif button == "3":
            typed = typed + "3"
         elif button == "4":
            typed = typed + "4"
         elif button == "5":
            typed = typed + "5"
         elif button == "6":
            typed = typed + "6"
         elif button == "7":
            typed = typed + "7"
         elif button == "8":
            typed = typed + "8"
         elif button == "9":
            typed = typed + "9"
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
         elif button == "mod":
            if wholeOp != "":
               wholeOp = str(calculator.calculate(wholeOp + typed))
               wholeOp = wholeOp + " % "
               modFlag = True
            else:
               wholeOp = typed + " % "
            typed = ""
         elif button == "div":
            if typed == "":
               pass
            else:
               if modFlag == True:
                  wholeOp = wholeOp + typed
                  wholeOp = str(calculator.calculate(wholeOp + typed))
               wholeOp = wholeOp + typed + " / "
               typed = ""
         elif button == "mul":
            if typed == "":
               pass
            else:
               if modFlag == True:
                  wholeOp = wholeOp + typed
                  wholeOp = str(calculator.calculate(wholeOp + typed))
               wholeOp = wholeOp + typed + " x "
               typed = ""
         elif button == "sub":
            if typed == "":
               pass
            else:
               if modFlag == True:
                  wholeOp = wholeOp + typed
                  wholeOp = str(calculator.calculate(wholeOp + typed))
               wholeOp = wholeOp + typed + " - "
               typed = ""
         elif button == "add":
            if typed == "":
               pass
            else:
               if modFlag == True:
                  wholeOp = wholeOp + typed
                  wholeOp = str(calculator.calculate(wholeOp + typed))
               wholeOp = wholeOp + typed + " + "
               typed = ""
         elif button == "equ":
            if typed == "":
               pass
            elif wholeOp == "":
               pass
            else:
               wholeOp = str(calculator.calculate(wholeOp + typed))
               typed = ""
               
   return render_template('ui.html', wholeOp=wholeOp, typed=typed)


if __name__ == "__main__":
   app.run(debug=True)