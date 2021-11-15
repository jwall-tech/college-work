def convert(numberList):
    index = 0
    for item in numberList:
        numberList[index] = str(item)
        index += 1
    return numberList

print(convert([1,2,3]))
