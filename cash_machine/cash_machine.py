class ATM():
    def __init__(self):
        self.balance = 0
        self.open = False
        self.pin = "1324"

    def requestOpen(self,pin):
        if self.pin == pin:
            self.open = True
            return True,"PIN SUCCESSFUL"
        return False,"INCORRECT PIN"

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return True,"WITHDRAW"
        else:
            return False,"INSUFFICIENT FUNDS"

    def deposit(self,amount):
        self.balance += amount
        return True,"DEPOSITED"

    def display(self):
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        print("Available Balance: "+str(self.balance))

myAtm = ATM()

while True:
    print("\n\n\n")
    if myAtm.open:
        myAtm.display()
        uInput = input(">>> ")
        if uInput == "1":
            newInput = input("Amount\n>>> ")
            newInput = int(newInput)
            print(myAtm.deposit(newInput)[1])
            
        elif uInput == "2":
            newInput = input("Amount\n>>> ")
            newInput = int(newInput)
            print(myAtm.withdraw(newInput)[1])

        elif uInput == "3":
            exit()
    else:
        myAtm.requestOpen(input("Pin\n>>> "))
