
row1 = {
    "head" : "",
    "cols" : ["Is it mutable?","Can we change the size after creation?", "Can items in the list be changed?","How many different types of data can be stored?","afanwanianbgiabgiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiwagbwaihgbawhgbhawibghiawbgiaihwabgihawbhigbahigbaii"],
}

row2 = {
    "head" : "List",
    "cols" : ["True","True", "True","All","a"],
}

row3 = {
    "head" : "Array",
    "cols" : ["True","False", "True","5","b"],
}

row4 = {
    "head" : "Tuple",
    "cols" : ["False","True", "True","2","caifjwaogoagabgiawbgiabi"],
}

rows = [row1,row2,row3,row4]

minRowWidth = 15
maxRowWidth = 15
global hasNext
global nextRows
global rowLength
nextRows = []
rowLength = 0
hasNext = False

def isEmpty(tbl):
    empty = True
    for item in tbl:
        if item != "":
            empty = False
        
    return empty

def print_rows(rows):
    rowSep = "_______________________________________________________________________"
    global nextRows

    def setSep():
        rowSep = ""
        for i in range(rowLength):
            rowSep += "_"
        return rowSep
            
    def checkHasNext():
        global hasNext
        global nextRows

        if hasNext and not isEmpty(nextRows):
            hasNext = False
            print("\n",end="")
            newNext = []
            for row in nextRows:
                nextRows = []
                if len(row) > maxRowWidth:
                    splitIndex = maxRowWidth-len(row)
                    newNext.append(row[splitIndex:])
                    row = row[:splitIndex]
                    hasNext = True
                    #print(row,newNext)
                else:
                    newNext.append("")
                
                print_section(row,ignoreMin=False,ignoreMax=True)
            nextRows=newNext
            if hasNext:
                #print(nextRows)
                checkHasNext()
    
    def print_section(text,ignoreMin=False,ignoreMax=False):
        rowSep = setSep()
        global hasNext
        global nextRows
        global rowLength

        if len(text) < minRowWidth and not ignoreMin:
            for i in range(minRowWidth - len(text)):
                text += " "

        if len(text) > maxRowWidth and not ignoreMax:
            splitIndex = maxRowWidth - len(text)
            nextRows.append(text[splitIndex:])
            text = text[:splitIndex]
            hasNext = True
        else:
            nextRows.append("")
        #print(nextRows)
        rowLength = len(text)
        print(text,end=" | ")
        
    
    for row in rows:
        print_section(row["head"])
    nextRows = []
        
    print("\n"+rowSep)

    for index in range(5):
        for row in rows:
            print_section(row["cols"][index])
        checkHasNext()
        if not hasNext:
            nextRows = []
    
        print("\n"+rowSep)
        

    
print_rows(rows)
