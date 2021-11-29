import random
import timeit
Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def random_key():
    length = random.randint(1,10)

    key = ""

    return key.join((random.choice(Letters) for x in range(length)))

    #return key

def random_value():
    length = random.randint(1,25)

    key = ""

    return key.join((random.choice(Letters) for x in range(length)))
    
    #return key

def generate_dict(length):
    myDict = {}

    for i in range(length):
        key = random_key()
        val = random_value()
        myDict[key] = val

    return myDict



def add_dict_to_file(myDict,file):
    with open(file,"a") as f:
        f.write("\n\n")
        f.write("# ADDED DICT\n")
        f.write("myDict = {\n")
        for key in myDict:
            val = myDict[key]
            f.write('"'+str(key)+'" : "'+val+'",\n')
        f.write("}")
        f.close()

#newDict = generate_dict(1000)
#print(newDict)
#add_dict_to_file(newDict,"hash_file_test.py")


