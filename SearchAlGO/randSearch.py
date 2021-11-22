import random

def randSearch(dataSet,target):
    found = False

    while not found:
        choice = random.choice(dataSet)
        if choice == target:
            found = True
            return True
    return False


