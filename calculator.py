class Calculator:
    def __init__(self):
        self.wholeOperation = input("FORMAT: num (space) operator (space) num (space)...") #This will be an input parameter once we set up a UI with flask
        self.WholeOperationArr = [] # list for the formatted list with spaces removed
        self.operations = [] # This list will contain only the operators as single Char strings
        self.numbers = [] # This list will contain only the numbers as INT
        self.history = {} # NOT IMPLIMENTED but will be a dict with the wholeOperation string and the answer int
        
        self.formatOperation() # Takes in the inout sting and removes the spaces to make each num or operator its own item then places into proper list
        self.calc() # Iterates semi-recursivly through the num and op lists to perform the operations with PEMDAS in mind
        print(self.numbers) # Prints last item in num list which will be the answer
        
    def formatOperation(self):
        
        self.WholeOperationArr = self.wholeOperation.split() # Split the string into a usable listr that can then be split further
        
        for idx, i in enumerate(self.WholeOperationArr): # Iterate through the list with i as the list item and idx as the index of the item
            '''
                Since the string is formatted num (space) operator (space) num (space)... with the spaces removed it will be
                num, op, num, op
                0  , 1 , 2  , 3 as the index
                so every even index will be a num while every odd will be an operator
                so when we iterate through the list we can append the even indexes to num, and the odd indexes to operators
            '''
            if idx % 2 == 0 or idx == 0:
                self.numbers.append(int(i))
            else:
                self.operations.append(i)
        
    def calc(self, counter = 0):
        '''
            will iterrate through the list of operators and do multiply and divide the first time
        '''
        for idx, i in enumerate(self.operations):
            if i == "*" or i == "x" or i == "X" or i == "/":
                if i == "*" or i == "x" or i == "X":
                    '''
                        When if finds an operator it takes the numbers that are at that index and the number one above that index
                        and plugs them into the right operation
                    '''
                    self.numbers[idx] = self.mult(self.numbers[idx], self.numbers[idx + 1])
                    '''
                        The number at the idex of the operator gets overwritten above while below the number that is one above gets
                        delted as well as the operator
                    '''
                    
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                elif i == "/":
                    self.numbers[idx] = self.div(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
            elif (i == "+" or i == "-") and counter > 0: # Counter so addition and subtraction get skipped the first time around
                if i == "+":
                    self.numbers[idx] = self.add(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                elif i == "-":
                    self.numbers[idx] = self.mult(self.numbers[idx], self.numbers[idx + 1])
                    del self.numbers[idx + 1]
                    del self.operations[idx]
                    
        if len(self.numbers) > 1: # If there are still numbers left the function has to run again but all mult and div should be done so counter ++
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
    