import _BaseDevice as Parent

class SmartHeat(Parent):
    def __init__(self):
        self.device_type = "Smart Heating"

        self.heat = 0

    def change_heat(self,newheat):
        self.heat = newheat
