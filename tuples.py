myTuple = ("hi",5,True,1.2)

myTupleAsString = str(myTuple)

def checkExists(tupe,item):
    for tItem in tupe:
        if item == tItem:
            return True
    return False

def sepIntoTupe():
    uInp = input(">>> ")
    return tuple(map(str, uInp))

print(myTuple)
print(myTupleAsString)
print(checkExists(myTuple,"hi"))
print(sepIntoTupe())
