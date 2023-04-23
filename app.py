from distutils.file_util import write_file
from flask import Flask, render_template, request, session
from calculator import Calculator


app = Flask(__name__)
app.secret_key = "my_secretKey"
calculator = Calculator()

#testing commit

typed = ""
wholeOp = ""
modFlag = False
latest = ""
middle = ""
oldest = ""

if modFlag == True:
   wholeOp = wholeOp + typed
   wholeOp = calculator.calculate(wholeOp)

@app.route("/", methods=['GET', 'POST'])
def homePage():
   
   global typed #double var
   global wholeOp #double var
   global modFlag #boolean 
   global latest
   global middle
   global oldest
   
   if request.method == "POST":
      # Get the button that was clicked
         button = request.form["button"]
         # Update the display screen based on the button clicked
         if button == "AC":
            wholeOp = ""
            typed = ""
            count = 0
         if button in "123456789":
            typed += button
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
               wholeOp = wholeOp + typed + " * "
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
               
               oldestEquation = str(f"{wholeOp + typed} = {calculator.calculate(wholeOp + typed)}")
               middleEquation = str(f"{wholeOp + typed} = {calculator.calculate(wholeOp + typed)}")
               latestEquation = str(f"{wholeOp + typed} = {calculator.calculate(wholeOp + typed)}")
               calculator.answerHistory.append(oldestEquation)
               calculator.answerHistory.append(middleEquation)
               calculator.answerHistory.append(latestEquation)
               oldest = calculator.answerHistory[2]
               middle = calculator.answerHistory[1]
               latest = calculator.answerHistory[0]
               wholeOp = str(calculator.calculate(wholeOp + typed))
               typed = ""
               
   return render_template('ui.html', wholeOp=wholeOp, typed=typed, latest=latest, middle=middle, oldest=oldest)


if __name__ == "__main__":
   app.run(debug=True)