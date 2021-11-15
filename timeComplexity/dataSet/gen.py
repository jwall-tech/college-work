import random
import time

oldtime = time.time()
with open("dataSet.csv","w") as f:
    f.write("age,life,num1,num2,num3,numb4,numb5")
    for i in range(500000):
        stCl = ""

        for i in range(7):
            stCl += str(random.randint(1,1000000))+","

        f.write("\n"+stCl)
    f.close()

print(time.time() - oldtime)
