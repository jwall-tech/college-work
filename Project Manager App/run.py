import os

class Project:
    Params = {
        "ProjectName" : "",
        "Deadline" : "",
        "Client" : "",
        "Price" : 0,
        "ProjectType" : "",
    }

    def _set(self,name,val):
        self.Params[name] = val

    def _get(self,name):
        if name in self.Params:
            return self.Params[name]
        return None
    
    def display(self):
        print("--------------------")
        for key in self.Params:
            val = self.Params[key]

            ps = "|  "+key+"  |>><<|  "+str(val)+"  |"
            print(ps)

        print("---------------------")

    def save(self):
        with open("saved.txt","a") as f:
            valst = ""
            for paramName in self.Params:
               val = self.Params[paramName]

               valst += paramName+":"+str(val)

               valst += ","
            valst += "\n"
            f.write(valst)
            print(valst)
            f.close()
               

               

class WebProj(Project):
    Params = {
        "ProjectName" : "",
        "Deadline" : "",
        "Client" : "",
        "Price" : 0,
        "ProjectType" : "Web",
        "ServerName" : "",
        "NumbPages" : 0,
    }
    
class App(Project):
    Params = {
        "ProjectName" : "",
        "Deadline" : "",
        "Client" : "",
        "Price" : 0,
        "ProjectType" : "App",
        "Type" : ""
    }

class Game(Project):
    Params = {
        "ProjectName" : "",
        "Deadline" : "",
        "Client" : "",
        "Price" : 0,
        "ProjectType" : "Game",
        "Platform" : "",
        "Genre" : "",
    }

class Menu:
    PageNumber = 0
    Apps = []
    Running = False

    def GetParams(self,cls):
        Params = cls.Params

        try:
            Params.pop("ProjectType")
        except:
            pass
    
        return Params
    
    def Page0(self):
        print("""
- Enter a new website (1)
- Enter a new app (2)
- Enter a new game (3)
- Display website (4)
- Display app (5)
- Display game (6)
- Display type (7)
- Display All(8)
- Help (9)
- Exit (10)
        """)

        UserInput = input(">>> ")

        if int(UserInput) <= 10 and int(UserInput) >= 0:
            self.PageNumber = int(UserInput)
        else:
            print("Invalid Bounds")

    def Page1(self):
        # New Web
        NewClass = WebProj()
        Vars = self.GetParams(NewClass)
        print(Vars)
        for var in Vars:
            print(type(Vars[var]))
            UInput = input(var+": ")
            if type(Vars[var]) == int:
                UInput = int(UInput)
            NewClass._set(var,UInput)

        NewClass._set("ProjectType","Web")
        
        NewClass.display()
        self.Apps.append(NewClass)
            
        self.PageNumber = 0

    def Page2(self):
        # New App
        NewClass = App()
        Vars = self.GetParams(NewClass)

        for var in Vars:
            print(type(Vars[var]))
            UInput = input(var+": ")
            if type(Vars[var]) == int:
                UInput = int(UInput)
            NewClass._set(var,UInput)

        NewClass._set("ProjectType","App")
        
        NewClass.display()
        self.Apps.append(NewClass)
            
        self.PageNumber = 0

    def Page3(self):
        # New Game
        NewClass = Game()
        Vars = self.GetParams(NewClass)

        for var in Vars:
            print(type(Vars[var]))
            UInput = input(var+": ")
            if type(Vars[var]) == int:
                UInput = int(UInput)
            NewClass._set(var,UInput)

        NewClass._set("ProjectType","Game")
        
        NewClass.display()
        self.Apps.append(NewClass)
            
        self.PageNumber = 0

    def Display(self,name):
        os.system("cls")
        for cls in self.Apps:
            if cls._get("ProjectName") == name:
                cls.display()

    def DisplayTypes(self,ptype):
        os.system("cls")
        for cls in self.Apps:
            if cls._get("ProjectType") == ptype:
                cls.display()

        self.PageNumber = 0

    def DisplaySetup(self,dtype):
        if dtype == "type":
            UserInp = input("Type Param: ")
            self.DisplayTypes(UserInp)
        else:
            UserInp = input("Name Param: ")
            self.Display(UserInp)

        self.PageNumber = 0
    
    def Page4(self):
        self.DisplaySetup("")

    def Page5(self):
        self.DisplaySetup("")

    def Page6(self):
        self.DisplaySetup("")

    def Page7(self):
        self.DisplaySetup("type")

    def Page8(self):
        for app in self.Apps:
            app.display()

        self.PageNumber = 0
    
    def Page9(self):
        print("help")

    def Page10(self):
        self.Running = False

    def DisplayCurrentPage(self):
        currentPage = self.PageNumber

        Methods = [method for method in dir(Menu) if method == "Page"+str(currentPage)]
        for method in Methods:
            myMethod = getattr(self,method)
            myMethod()

MyMen = Menu()
MyMen.Running = True

with open("saved.txt","r") as f:
    lines = f.readlines()

    for line in lines:

        dictInps = line.split(",")

        Mdict = {}
        
        for inp in dictInps:
            newInp = inp.split(":")

            if len(newInp) == 2:
                key = newInp[0]
                val = newInp[1]

                Mdict[key] = val

        projType = Mdict["ProjectType"]

        c = None
        if projType == "Web":
            c = WebProj
        elif projType == "App":
            c = App
        elif projType == "Game":
            c = Game

        child = c()
        child.Params = Mdict

        MyMen.Apps.append(child)
            

while MyMen.Running:
    os.system("PAUSE")
    os.system("cls")
    try:
        MyMen.DisplayCurrentPage()
    except Exception as e:
        print(e)
        MyMen.PageNumber = 0

open("saved.txt","w").close()
for app in MyMen.Apps:
    app.save()
