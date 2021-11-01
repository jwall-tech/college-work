intList = [1,2,3,4,5]
strList = ["one","two","three","four","five"]

print(intList,strList)

intList.reverse()

print(intList,strList)

strList.extend(intList)

print(intList,strList)

squaredInt = []

for integer in intList:
    squaredInt.append(integer**2)

print(intList,squaredInt)


mergeList = zip(squaredInt,strList)

print(mergeList)
