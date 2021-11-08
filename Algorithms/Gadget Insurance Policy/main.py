##################
# Module Imports #
##################

##################
# Variables      #
##################

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
    print("0. Exit")

def NewPolicy():
    print("Input in order (client name,reference,number of gadgets,most expensive gadget value,excess,payment terms")
    UserInput = input(">>> ")
    InputTable = UserInput.split(",")
    
    Prem = WorkOutPremium(int(InputTable[2]),int(InputTable[3]),int(InputTable[4]),InputTable[5])
    if Prem:
        PrintSummary(InputTable[0],"08/11/2021",InputTable[5],int(InputTable[4]),Prem,1000,InputTable[1],int(InputTable[2]))
    else:
        Prem = 0
        InputTable[5] = "REJECTED"
    InputTable.append(str(Prem))
    InputTable.append(str("08/11/2021"))
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
