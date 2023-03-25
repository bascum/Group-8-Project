class Calculator:
    def __init__(self):
        self.wholeOperation = input("FORMAT: num (space) operator (space) num (space)...")
        self.WholeOperationArr = []
        self.operations = []
        self.numbers = []
        self.history = []
        
        self.formatOperation()
        self.calc()
        print(self.numbers)
        
    def formatOperation(self):
        self.WholeOperationArr = self.wholeOperation.split()
        for idx, i in enumerate(self.WholeOperationArr):
            if idx % 2 == 0 or idx == 0:
                self.numbers.append(int(i))
            else:
                self.operations.append(i)
        
    def calc(self, counter = 0):
        for idx, i in enumerate(self.operations):
            if i == "*" or i == "x" or i == "X" or i == "/":
                if i == "*" or i == "x" or i == "X":
                    self.numbers[idx] = self.mult(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                elif i == "/":
                    self.numbers[idx] = self.div(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
            elif (i == "+" or i == "-") and counter > 0:
                if i == "+":
                    self.numbers[idx] = self.add(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                elif i == "-":
                    self.numbers[idx] = self.mult(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                    
        if len(self.numbers) > 1:
            counter += 1
            self.calc(counter)

    def add(self, num1, num2):
        return num1 + num2
    
    def sub(self, num1, num2):
        return num1 - num2
    
    def mult(self, num1, num2):
        return num1 * num2
    
    def div(self, num1, num2):
        return num1 / num2
    