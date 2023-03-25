class Calculator:
    def __init__(self):
        self.currentOp
        self.history = []
        
    def calc(self, num1, operation, num2):
        if operation == "+":
            self.add(num1, num2)
        elif operation == "-":
            self.sub(num1, num2)
        elif operation == "*":
            self.mult(num1, num2)
        elif operation == "/":
            self.div(num1, num2)
            
    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mult(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 / num2
    