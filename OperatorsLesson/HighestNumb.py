def getHighest(table):
    highest = 0
    for item in table:
        item = int(item)
        if item > highest:
            highest = item
    return highest

while True:
    print("Enter 3 Numbers Seperated By a Space")
    numtable = input().split(" ")
    print(getHighest(numtable))
