###
# Module Imports
###
import random
import os
import pyttsx3

###
# Response Tree for bot responses depending on catagory
# CATAGORY : POSSIBLE_RESPONSES
###
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

###
# User Inputs that relate to certain responses
# CATAGORY : POSSIBLE_USER_INPUTS
###
textResponses = {
    "Greetings" : ["hi","hello","hiya","sup","whatup"],
    "Goodbye" : ["bye","goodbye","see ya","laters"],
    "HowU" : ["how are you","hows you","hru","how are you doing","whats up","what up"],
    "Quest" : ["ask me a question","question","give question"],
    "Positive" : ["im good","great","good","fine","ok"],
    "Negative" : ["im bad","bad","terrible","crap","not good"],
}

# Clears console screen
def clearScreen():
    os.system("cls")

# Gets user input
def getUserInput():
    clearScreen()
    print(BotName)
    UserInput = input("\n>>> ") ## \n is the break line, starts the input text on a new line
    return UserInput # Returns the input as a variable to wherever function was called

###
# Using classes just because im ard
###
class Chatty:
    ###
    # Init is a method
    # __init__ is ran whenever a new class is initiated
    ###
    def __init__(self,name):
        self.name = name
        self.engine = pyttsx3.init()
        
        ## Chatty Loop
        ###
        # Loop without an end, runs until program is closed
        ###
        while True:
            uInput = getUserInput()
            if uInput == "--help":
                # if user inputs --help then it prints all the user inputs
                print(textResponses)
                os.system("PAUSE")
            else:
                # runs the get reply function, prints the reply and pauses the code
                botReply = self.getReply(uInput)
                print(self.name+": "+botReply)
                self.engine.say(botReply)
                self.engine.runAndWait()
                os.system("PAUSE")

    ###
    # This function loops through the two tables at the top of the code
    # looks to see if the user input matches the tables and if it does then it either prints a response or does a thing
    # the question bit asks the user a question with a new section and gives a response
    ###
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
    
###
# Initiates the class Chatty
# Pauses the code when the loop ends
###
BotName = "BDOG"
myChatty = Chatty(BotName)
os.system("PAUSE")
