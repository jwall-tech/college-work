def CH1():
    with open("newFile.txt","w") as f:
        f.write("Hello 50 @")
        f.close()


def CH2(data):
    with open("newFile.txt","a") as f:
        f.write("\n")
        f.write(data)
        f.close()

def CH3(data):
    with open("newFile.txt","r") as f:
        saved = f.read()
        f.close()

    with open("newFile.txt","w") as f:
        f.write(data + " " + saved)
        f.close()

def CH4(data):
    with open("newFileList.txt","w") as f:
        for item in data:
            f.write(item+"\n")
        f.close()

def CH5():
    with open("gamerscore.csv","r") as f:
        for line in f.readlines():
            handle,score = line.split(",")
            print("Handle: "+handle+"\nScore: "+score)
        f.close()

CH1()
CH2("LOL")
CH3("hi")
CH4(["hi","billy","marsh"])
CH5()
