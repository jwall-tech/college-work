class Base():
    _components = {}

    def GetComponent(self,key):
        if key in self._components:
            return self._components[key]
        else:
            return None

    def SetComponent(self,key,value,overwrite=True):
        if key in self._components:
            if not overwrite:
                return False

        self._components[key] = value
        return True


myClass = Base()

myClass.SetComponent("hi",5)
Comp = myClass.GetComponent("hi")
print(Comp)
myClass.SetComponent("hi",54)
Comp = myClass.GetComponent("hi")
print(Comp)
