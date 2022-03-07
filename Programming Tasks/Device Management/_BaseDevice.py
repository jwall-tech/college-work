class Device:
    def __init__(self,*args,**kwargs):
        pass
    
    def Activate(self):
        self.device_active = True

    def Deactivate(self):
        sefl.device_active = False
