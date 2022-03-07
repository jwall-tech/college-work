import _BaseDevice as Parent

class SmartLight(Parent):
    def __init__(self):
        self.device_type = "Smart Light"

        self.light_intensity = 0
        self.light_colour = "red"

    def change_colour(self,newcolour):
        self.light_colour = newcolour

    def change_intensity(self,newint):
        self.light_intensity = newint
