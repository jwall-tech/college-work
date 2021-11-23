import random
fruits = ["a","b","c","d"]

def same(t1,t2):
    yes = False
    for item in t1:
        if item in t2:
            yes = True
        else:
            yes = False
            return yes

    for item in t2:
        if item in t1:
            yes = True
        else:
            yes = False
            return yes
    return yes

def find(elements,value):
    indexesFound = []

    while not same(indexesFound,elements):
        rand = random.randint(0,len(elements))-1
        if not elements[rand] in indexesFound:
            indexesFound.append(elements[rand])
        if elements[rand] == value:
            return rand
        print(elements[rand],value,indexesFound)
        return False

print(find(fruits,"x"))
