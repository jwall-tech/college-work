class BankingAPI:
    def __init__(self,accounts):
        self.accounts = accounts

    def get(self,cardNumb,pinNumb):
        ind = 0
        for acc in self.accounts:
            if acc["CardNumber"] == cardNumb:
                if acc["PinNumber"] == pinNumb:
                    return ind,"Correct Pin"
                else:
                    return False,"Incorrect Pin"
            ind += 1
        return False,"Card Number Not Recognised"
    
    def withdraw(self,cardNumb,pinNumb,amount):
        account = self.get(cardNumb,pinNumb)

        account = account[0]
        if account:
            accountBal = self.accounts[account]["Balance"]
            if accountBal >= amount:
                self.accounts[account]["Balance"] -= amount
                return True,self.accounts[account]["Balance"]
            else:
                return False,"Insufficient Balance"
        else:
            return False,"Account Error"

    def deposit(self,cardNumb,pinNumb,amount):
        account = self.get(cardNumb,pinNumb)

        account = account[0]
        if account:
            self.accounts[account]["Balance"] += amount
            return True,self.accounts[account]["Balance"]
        else:
            return False,"Account Error"

    def account(self,cardNumb,pinNumb):
        getReq = self.get(cardNumb,pinNumb)
        if getReq[0]:
            return self.accounts[getReq[0]]
        else:
            return False,"Account Error"

class ATM:
    def __init__(self,bank):
        self.open = False
        self.cardNumb = ""
        self.pinNumb = ""
        self.bank = bank

    def authorise(self,cardNumb,pinNumb):
        getReq = self.bank.get(cardNumb,pinNumb)

        if getReq[0]:
            self.open = True
            self.cardNumb = cardNumb
            self.pinNumb = pinNumb
            print(getReq[1])
        else:
            print(getReq[1])
        return getReq

    def display(self):
        if self.open:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Logout")
            print("4. Exit")
            
            userAccount = self.bank.account(self.cardNumb,self.pinNumb)
            if userAccount:
                print(userAccount["Balance"])
            else:
                print(userAccount[1])
        else:
            print("NOT LOGGED IN")

    def deposit(self,*args,**kwargs):
        if self.open:
            depReq = self.bank.deposit(self.cardNumb,self.pinNumb,*args,**kwargs)
            
            if depReq:
                print("DEPOSITED\nNEW BALANCE: "+str(depReq[1]))
            else:
                print(depReq[1])
        else:
            print("NOT LOGGED IN")

    def withdraw(self,*args,**kwargs):
        if self.open:
            withReq = self.bank.withdraw(self.cardNumb,self.pinNumb,*args,**kwargs)
            
            if withReq:
                print("WITHDREW\nNEW BALANCE: "+str(withReq[1]))
            else:
                print(withReq[1])
        else:
            print("NOT LOGGED IN")

accounts = [
    {
        "CardNumber" : "5523 2212 4422",
        "PinNumber" : "1234",
        "CCV" : "142",
        "Balance" : 100
    },
    
    {
        "CardNumber" : "5511 2222 5522",
        "PinNumber" : "2434",
        "CCV" : "169",
        "Balance" : 500
    },
    
    {
        "CardNumber" : "3312 1143 4627",
        "PinNumber" : "9999",
        "CCV" : "123",
        "Balance" : 200000
    },
]


myBank = BankingAPI(accounts)
myATM = ATM(myBank)

while True:
    if myATM.open:
        myATM.display()

        userInput = input(">>> ")

        if userInput == "1":
            amount = int(input("Amount\n>>> "))
            myATM.deposit(amount)
        elif userInput == "2":
            amount = int(input("Amount\n>>> "))
            myATM.withdraw(amount)
        elif userInput == "3":
            myATM.open = False
        elif userInput == "4":
            exit()
    else:
        print("MUST AUTHORISE")
        cardNumb = input("Card Number\n>>> ")
        print("\n")
        pinNumb = input("Pin Number\n>>> ")
        print("\n")

        authorReq = myATM.authorise(cardNumb,pinNumb)
