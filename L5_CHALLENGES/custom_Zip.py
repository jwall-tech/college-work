def zap(*args):
    bigLength = 0
    endTbl = []
    for item in args:
        if len(item) > bigLength:
            bigLength = len(item)
    print(bigLength)
    for index in range(bigLength):
        arr = []

        for tbl in args:
            if len(tbl) < bigLength and index == len(tbl):
                break
            arr.append(tbl[index])
                
        endTbl.append(arr)
    return endTbl
        

print(zap([1,2,3],[4,5,6],[7,8,9],[1,2]))
