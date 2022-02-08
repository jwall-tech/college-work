def CSV_To_Table(file):
    ReturnTable = []
    with open(file,"r") as f:
        Rows = f.readlines()
        if len(Rows) <= 0:
            return None
        
        Titles = Rows[0].split(",")
        Rows.pop(0)

        for row in Rows:
            Collums = row.split(",")
            
            count = 0
            
            rowDict = {}

            for title in Titles:
                if len(Collums) > count+1:
                    title = title.split("\n")[0]
                    myCol = Collums[count]
                    count += 1
                    rowDict[title] = myCol

            ReturnTable.append(rowDict)
        f.close()
    return ReturnTable

def Table_To_CSV(file,table):
    if len(table) <= 0:
        with open(file,"w") as f:
            f.write("prodid,name,department,location,quantity,price,pricevat\n")
            f.close()
            return None
    #print("TB::",table)
    with open(file,"w") as f:
        f.write("prodid,name,department,location,quantity,price,pricevat\n")

        for myDict in table:
            for key in myDict:
                print(key)
                val = myDict[key]
                #print(myDict)
                if len(myDict)-1 == list(myDict.keys()).index(key):
                    f.write(val+"\n")
                else:
                    f.write(val+",")
        f.close()
    return True

def Add_To_CSV(file,dicta):
    CurrentData = CSV_To_Table(file)
    #print("CD::",CurrentData)
    if CurrentData:
        pass
    else:
        CurrentData = []

    CurrentData.append(dicta)
    Table_To_CSV(file,CurrentData)

def Remove_From_CSV(file,searchFunc):
    CurrentData = CSV_To_Table(file)

    if CurrentData:
        Count = 0
        for Row in CurrentData:
            if searchFunc(Row):
                CurrentData.pop(Count)
            Count += 1

        Table_To_CSV(file,CurrentData)
