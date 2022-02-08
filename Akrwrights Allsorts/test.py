import CSVparse
import random
import os

for i in range(1,100):
    prid = ""
    for i2 in range(7):
        prid += str(random.randint(1,9))

    name = "Test"+str(i)

    department = random.choice(["Power tools", "Power tool accessories", "Hand tools", "Tool storage", "Measuring tools", "Testing equipment", "Heating & plumbing", "electrical & lighting and screws", "nails & fixings"])

    location = random.choice(["A","B","C","D","E","F"]) + str(random.randint(1,9))

    quantity = random.randint(1,1000)

    price = random.randint(1,10000000)

    pricevat = price+10

    quantity = str(quantity)
    price = str(price)
    pricevat = str(pricevat)
    os.system("PAUSE")
    a = CSVparse.Add_To_CSV("data.csv",{
        "prodid" : prid,
        "name" : name,
        "department" : department,
        "location" : location,
        "quantity" : quantity,
        "price" : price,
        "pricevat" : pricevat
        })
    print("tb2:::",{
        "prodid" : prid,
        "name" : name,
        "department" : department,
        "location" : location,
        "quantity" : quantity,
        "price" : price,
        "pricevat" : pricevat
        })
    print("Added info (ID: "+prid+")")

print(CSVparse.CSV_To_Table("data.csv"))
