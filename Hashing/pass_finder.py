urPass = "f76b61b962db075bb76ad6f3fab10f7bd546f92f1b89f18c513d4122575c18ac"
import hashlib

with open("plainTextPass.txt","r") as f:
    lines = f.readlines()

    for mPass in lines:
        #mPass = mPass[:len(mPass)-1]
        break
        hashedPass = hashlib.sha256(mPass.encode()).hexdigest()
        if hashedPass == urPass:
            print(mPass)

    f.close()
