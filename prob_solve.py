generic_tree = {
    "question" : "Powers or Tech?",

    "op1" : {
        "question" : "Lightning Powers",

        "op1" : "thor",
        
        "op2" : {
            "question" : "Male or Female",

            "op1": "Superman",
            "op2": "Wonder Woman",

            "op1_name": "male",
            "op2_name": "female",
        },

        "op1_name" : "yes",
        "op2_name" : "no"
    },
    
    "op2" : {
        "question" : "Flies",

        "op1" : "ironman",
        
        "op2" : "batman",

        "op1_name" : "yes",
        "op2_name" : "no"
    },

    "op1_name" : "powers",
    "op2_name" : "tech"
}

def format_question(tab):
    print(tab["question"])
    print(tab["op1_name"])
    print(tab["op2_name"])
    userInp = input(">>> ")

    nxt = get_next(tab,userInp)
    if type(nxt) == dict:
        format_question(nxt)
    else:
        print(nxt)

def get_next(tab,ans):
    if tab["op1_name"] == ans:
        return tab["op1"]
    elif tab["op2_name"] == ans:
        return tab["op2"]
    else:
        print("wrong")
        return False


format_question(generic_tree)

