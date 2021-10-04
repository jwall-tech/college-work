print("CALCY V1.0")

class Calcy():
    def __init__(self):
        ## Calc Loop
        while True:
            userInput = input("Sum String\n>>> ")
            splitTable = userInput.split()

            step = 1

            previousNumb = 0
            currentOperator = "+"
            
            try:       
                for value in splitTable:
                    if step  % 2:
                        if previousNumb == None:
                            previousNumb = int(value)
                        else:
                            value = int(value)
                            previousNumb = self.runFuncFromOperator(currentOperator,previousNumb,value)
                    else:
                        currentOperator = value

                    step += 1
            except:
                print("has to be number")

            print("YOUR ANSWER: "+str(previousNumb))

    def runFuncFromOperator(self,operator,*args):
        if operator == "+":
            return self.Add(*args)
        elif operator == "-":
            return self.Subtract(*args)
        elif operator == "/":
            return self.Divide(*args)
        elif operator == "*":
            return self.Multiply(*args)

    def Add(self,num1,num2):
        return num1 + num2

    def Divide(self,num1,num2):
        if num2 != 0 and num1 != 0:
            return num1 / num2
        else:
            print("Can't divide by 0")
            return "DIV ERROR, CANT DIVIDE BY 0"

    def Multiply(self,num1,num2):
        return num1 * num2

    def Subtract(self,num1,num2):
        return num1 - num2

CalcyBoy = Calcy()
