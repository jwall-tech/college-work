from abc import ABC
import struct

class Shape(ABC):
    args = {}
    def calculate_area(self):
        pass

    def calculate_perim(self):
        pass

    def _set_param(self,a,b):
        self.args[a] = b


class Square(Shape):
    def __init__(self,length=0,width=0):
        pass

    def calculate_area(self):
        return self.args["length"] * self.args["width"]

    def calculate_perim(self):
        return self.args["length"] * 4
        

class Circle(Shape):
    def __init__(self,radius=0):
        pass

    def calculate_area(self):
        return 3.14 * self.args["radius"] * self.args["radius"]

    def calculate_perim(self):
        pass

    def calculate_circumf(self):
        return 2 * 3.14 * self.args["radius"]

class Triangle(Shape):
    def __init__(self,Base=0,Height=0,A=0,B=0,C=0):
        self.Base = Base
        self.Height = Height
        self.A,B,C = A,B,C

    def calculate_area(self):
        return (self.args["Base"]*self.args["Height"])/2

    def calculate_perim(self):
        return self.args["A"] + self.args["B"] + self.args["C"]    
    
class Rectangle(Shape):
    def __init__(self,length=0,width=0):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.args["length"] * self.args["width"]

    def calculate_perim(self):
        return 2*(self.args["width"] + self.args["length"])    

class Cube(Shape):
    def __init__(self,side=0):
        self.side = side

    def calculate_area(self):
        return (self.args["side"] * 6) ** 2

    def calculate_perim(self):
        return self.args["side"] * 12
    
class Rhombus(Shape):
    def __init__(self,side=0,product_of_diags=0):
        self.side = side
        self.product_of_diags = product_of_diags
        
    def calculate_area(self):
        return 0.5 * self.args["product_of_diags"]
    
    def calculate_perim(self):
        return self.args["side"] * 4

class Cher(Shape):
    def __init__(self,teacher=0,hi=0):
        pass

    def yes(self):
        return self.args["teacher"] * self.args["hi"]
        

classes = [Circle,Triangle,Square,Rectangle,Cube,Rhombus,Cher]

def getClass(name):
    for clss in classes:
        if clss.__name__ == name:
            return clss
    return False

def DisplayMenu():
    print("Shapes")
    print("Circle,Triangle,Square,Rectangle,Cube,Rhombus,Cher")
    uInput = input(">>> ")
    Class = getClass(uInput)
    if Class:
        ParamNames = Class.__init__.__code__.co_varnames

        Args = {}
        Tab = []
        
        for Param in ParamNames:
            if Param != "self":
                Uinput =input(Param+": ")
                Args[Param] = Uinput
                Tab.append(Uinput)
                
        Child = Class()
        for name in Args:
            val = Args[name]
            Child._set_param(name,int(val))

        MethodNames = [method for method in dir(Class) if (method.startswith('_') or method == "args") is False]

        while True:
            print(MethodNames)
            uInput = input(">>> ")
            if uInput in MethodNames:
                method = getattr(Child,uInput)
                print(method())
            else:
                break

while True:
    DisplayMenu()
    
