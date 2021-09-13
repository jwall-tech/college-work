import random
import os

responseTree = {
    "Greetings" : ["Hey there!","Hiya!"],
    "Goodbye" : ["See you later!","Goodbye!"],
    "Positive" : ["That's great!","Good!"],
    "Negative" : ["Oh no!","Shame!"],
    "Convo" : [],
    "HowU" : ["I'm good, you?","I am great, how are you?"],
    "Quest" : ["What is 2 + 2","What is billy"],
    "QuestAns" : ["4","smelly"],
}

textResponses = {
    "Greetings" : ["hi","hello","hiya","sup","whatup"],
    "Goodbye" : ["bye","goodbye","see ya","laters"],
    "HowU" : ["how are you","hows you","hru","how are you doing","whats up","what up"],
    "Quest" : ["ask me a question","question","give question"],
    "Positive" : ["im good","great","good","fine","ok"],
    "Negative" : ["im bad","bad","terrible","crap","not good"],
}

BotName = "Billy"

COLORS = {\
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
    }
    
def colorText(text,color):
    text = text.replace("[["+color+"]]",COLORS[color])
    return text

def clearScreen():
    os.system("cls")

def getUserInput():
    clearScreen()
    print(colorText(BotName,"red"))
    UserInput = input("\n>>> ")
    return UserInput

class Chatty:
    def __init__(self,name):
        self.name = name

        ## Chatty Loop
        while True:
            uInput = getUserInput()
            if uInput == "--help":
                print(textResponses)
                os.system("PAUSE")
            else:
                botReply = self.getReply(uInput)
                print(self.name+": "+botReply)
                os.system("PAUSE")
            
    def getReply(self,text):
        for catName in textResponses:
            catTable = textResponses[catName]
            if catName == "Quest":
                if text.lower() in catTable:
                    responseTable = responseTree[catName]
                    answerTable = responseTree["QuestAns"]

                    questionInd = random.randint(0,len(responseTable)-1)

                    quest = responseTable[questionInd]
                    answer = answerTable[questionInd]
                    
                    qInput = input(quest)
                    
                    if qInput.lower() == answer.lower():
                        print("CORRECT! WELL DONE!")
                    else:
                        print("WRONG! Correct Answer: "+answer)
                    return ""
            else:    
                if text.lower() in catTable:
                    responseTable = responseTree[catName]
                    response = responseTable[random.randint(0,len(responseTable)-1)]
                    return response
    

myChatty = Chatty(BotName)
os.system("PAUSE")
