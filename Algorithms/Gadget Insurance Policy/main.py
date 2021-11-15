##################
# Module Imports #
##################
import re
import random
##################
# Variables      #
##################
date = "15/11/2021"
##################
# Functions      #
##################
def PrintSummary(client,date,terms,excess,anprm,lpg,ref,items):
    List = """
+==========================================+
|                                          |
| Client: CL                          
|                                          |
| Date: DT            
| Terms: TRMS            Items: ITMS                
| Excess: £EX            Ref: RF               
|                                          |
| TYPE                 Limit per                         
| Premium: £ANP       Gadget: LPG            
|                                          |
+==========================================+
"""

    itable = ["One","Two","Three","Four","Five"]

    if items < 6:
        items = itable[items-1]
    
    List = List.replace("CL",client)
    List = List.replace("DT",str(date))
    List = List.replace("TRMS",str(terms))

    List = List.replace("EX",str(excess))
    List = List.replace("ANP",str(anprm))
    List = List.replace("LPG",str(lpg))

    List = List.replace("ITMS",str(items))
    List = List.replace("RF",str(ref))
    List = List.replace("TYPE", str(terms.upper()))

    print(List)

def WorkOutPremium(numb_items,max_gadg,excess,typ):
    discount = 0
    if typ == "annual":
        discount += 10

    if excess > 30:
        amount = excess - 30
        amount /= 10
        discount += (5*amount)
    price = 0
    if numb_items == 1:
        if max_gadg <= 500:
            price = 5.99
        elif max_gadg <= 800:
            price = 7.15
        elif max_gadg <= 1000:
            price = 8.30
        else:
            return False
    elif numb_items <= 3:
        if max_gadg <= 500:
            price = 10.99
        elif max_gadg <= 800:
            price = 13.35
        elif max_gadg <= 1000:
            price = 15.55
        else:
            return False
    elif numb_items <= 5:
        if max_gadg <= 500:
            price = 15.99
        elif max_gadg <= 800:
            price = 19.60
        elif max_gadg <= 1000:
            price = 22.82
        else:
            return False
    else:
        return False

    if typ == "annual":
        price *= 12
    print(price)
    price *= (1 - (discount / 100))
    return round(price,2)

def PrintMenu():
    print("1. Enter new policy")
    print("2. Display Summary of Policies")
    print("3. Display Summary of Policies for Selected Month")
    print("4. Find and display Policy")
    print("5. Debug Add Random")
    print("0. Exit")

def NewPolicy(i=None,d=None):
    print("Input in order (client name (John H Smith),reference (JB123A) ,number of gadgets,most expensive gadget value,excess,payment terms")
    UserInput = i or input(">>> ")
    InputTable = UserInput.split(",")

    RefNumb = InputTable[1]

    pattern = r"\D\D\d\d\d\D"

    if not re.match(pattern,RefNumb):
        print("WRONG FORMAT MUST BE 2 LETTERS, 3 NUMBERS, 1 LETTER EXAMPLE: JB123A")
        return None
    
    Prem = WorkOutPremium(int(InputTable[2]),int(InputTable[3]),int(InputTable[4]),InputTable[5])
    if Prem:
        PrintSummary(InputTable[0],d or date,InputTable[5],int(InputTable[4]),Prem,1000,RefNumb,int(InputTable[2]))
    else:
        Prem = 0
        InputTable[5] = "REJECTED"
    InputTable.append(str(Prem))
    InputTable.append(str(d or date))
    with open("policy.txt","a") as f:
        f.write("\n")
        index = 0
        for item in InputTable:
            index += 1
            item = item.replace(" ",",")
            if index >= len(InputTable):
                f.write(item)
            else:
                f.write(item + " ")
        

        f.close()

def ArchivePolicy():
    with open("policy.txt","r") as f:
        newData = f.read()
        f.close()

    with open("archive.txt","a") as f:
        f.write(newData)
        f.close()

    open("policy.txt","w").close()

def SummaryOfPolicies():
    fileName = input("archive or policy\n>>> ")
    if fileName == "archive" or fileName == "policy":
        with open(fileName+".txt") as f:
            lines = f.readlines()
            f.close()

            _perMonth = {
                "01" : 1,
                "02" : 0,
                "03" : 5,
                "04" : 0,
                "05" : 0,
                "06" : 19,
                "07" : 0,
                "08" : 22,
                "09" : 0,
                "10" : 0,
                "11" : 100,
                "12" : 0,
            }
            _months = {
                "01" : "Jan",
                "02" : "Feb",
                "03" : "Mar",
                "04" : "Apr",
                "05" : "May",
                "06" : "Jun",
                "07" : "Jul",
                "08" : "Aug",
                "09" : "Sep",
                "10" : "Oct",
                "11" : "Nov",
                "12" : "Dec",
            }
            _itemsInt = 0
            _mPremInt = 0
            for line in lines:
                if not line == "" and not line == "\n":
                    check = line.split(" ")
                    items = check[2]
                    premium = check[6]
                    date = check[7]

                    date_split = date.split("/")
                    date_month = date_split[1]
                    date_day = date_split[0]
                    date_year = date_split[2]

                    _perMonth[date_month] += 1
                    
                    _mPremInt += bool(premium)
                    _itemsInt += int(items)

            Total = len(lines)
            Average = round(_itemsInt / Total,2)
            Average_Premium = round(_mPremInt / Total,2)

            print("Total Number of policies: "+str(Total))
            print("Average number of items (Accepted): "+str(Average))
            print("Averge Premium: "+str(Average_Premium))
            print("Number of Policies Per Month: \n")

            for name in _perMonth:
                print(_months[name], end=" ")
            print("\n")
            for name in _perMonth:
                if _perMonth[name] > 9:
                    print(_perMonth[name],end="  ")
                elif _perMonth[name] > 99:
                    print(_perMonth[name],end=" ")
                else:
                    print(_perMonth[name],end="   ")
                
            print("\n")

def MonthPolicies():
    fileName = input("archive or policy\n>>> ")
    month = input("month\n>>> ")
    if fileName == "archive" or fileName == "policy":
        with open(fileName+".txt") as f:
            lines = f.readlines()
            f.close()

            _itemsInt = 0
            _mPremInt = 0
            Total = 1
            for line in lines:
                check = line.split(" ")

                items = check[2]
                premium = check[6]
                date = check[7]

                date_split = date.split("/")
                date_month = date_split[1]
                date_day = date_split[0]
                date_year = date_split[2]

                if date_month == month:
                    Total += 1
                    _mPremInt += bool(premium)
                    _itemsInt += int(items)

            Average = round(_itemsInt / Total,2)
            Average_Premium = round(_mPremInt / Total,2)

            print("Total Number of policies: "+str(Total-1))
            print("Average number of items (Accepted): "+str(Average))
            print("Averge Premium: "+str(Average_Premium))
            print("Number of Policies Per Month: \n")
                
            print("\n")

def FindDisplay():
    fileName = input("archive or policy\n>>> ")
    st = input("search term\n>>> ")
    if fileName == "archive" or fileName == "policy":
        with open(fileName+".txt") as f:
            lines = f.readlines()
            f.close()

            for line in lines:
                userData = line.split(" ")

                for dataPiece in userData:
                    for ind in range(len(dataPiece)-1):
                        if len(dataPiece) > ind:
                            if dataPiece[ind] == ",":
                                dataPiece = dataPiece[:ind+1] + " " + dataPiece[:ind-1]

                ClientName = userData[0]
                s1 = ClientName.split(",")
                ClientName = s1[0]+" "+s1[1]
                RefNumb = userData[1]
                
                check = line.split(" ")

                items = check[2]
                premium = check[6]
                date = check[7]

                date_split = date.split("/")
                date_month = date_split[1]
                date_day = date_split[0]
                date_year = date_split[2]

                if re.search(st,RefNumb) or re.match(st,ClientName):
                    PrintSummary(ClientName,date,"Annual",int(check[4]),bool(premium),1000,RefNumb,int(items))

def RandomAdd():
    fNames = ["John","James","Marco","Jacob","Moritz","Duncan","Chloe"]
    lNames = ["Smith","Wallace","Divine","Skilton","Corny","Jermy"]

    Letters = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
    Letters = Letters.split(",")

    payTerms = ["annual","monthly"]

    for i in range(20):
        Name = random.choice(fNames) + " " + random.choice(lNames)
        Ref = ""
        
        for i in range(2):
            Ref = Ref + random.choice(Letters)

        for i in range(3):
            Ref = Ref + str(random.randint(1,9))

        Ref = Ref + random.choice(Letters)

        Gadg = random.randint(1,1000)

        expens = random.randint(1,200)

        exc = random.randint(1,70)

        term = random.choice(payTerms)

        inpString = Name+","+Ref+","+str(Gadg)+","+str(expens)+","+str(exc)+","+str(term)

        m = random.randint(1,12)
        if m < 10:
            m = "0"+str(m)
        else:
            m = str(m)

        d = random.randint(1,30)

        if d < 10:
            d = "0"+str(d)
        else:
            d = str(d)
        
        date = d+"/"+m+"/"+"2021"
        
        NewPolicy(i=inpString,d=date)

    #ArchivePolicy()
    #exit()


while True:
    PrintMenu()

    UInput = input(">>> ")

    if UInput == "1":
        NewPolicy()
    elif UInput == "0":
        ArchivePolicy()
        exit()
    elif UInput == "2":
        SummaryOfPolicies()
    elif UInput == "3":
        MonthPolicies()
    elif UInput == "4":
        FindDisplay()
    elif UInput == "5":
        RandomAdd()
