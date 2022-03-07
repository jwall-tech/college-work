import importlib
import os

## Variables
device_active = True
device_state = "menu"
device_name = ""

## Functions
def GetDevicesList():
    dirLocation = "Devices/"
    dirList = os.listdir(dirLocation)

    returnList = []

    for item in dirList:
        if not item.startswith("_"):
            returnList.append(item)

    return returnList

def GetDevice(name):
    ListOfDevices = GetDevicesList()

    if name in ListOfDevices:
        return importlib.import_module("Devices."+name)

## Main Loop
while device_active:
    if device_state == "menu":
        print("""
            MENU
            1. DEVICE MENU
            2. QUIT
        """)

        userInput = input(">>> ")

        if userInput == "1":
            device_state = "devicesmenu"
        else:
            device_state = "quit"
            
    elif device_state == "devicesmenu":
        Devices = GetDevicesList()

        print("DEVICES")
        index = 0
        for item in Devices:
            print(str(index)+". "+item)
            index += 1

        UserInput = int(input(">>> "))

        if UserInput <= len(Devices)-1:
            Device = Devices[UserInput]
            device_state = "device"
            device_name = Device
        
    elif device_state == "device":
        deviceModule = GetDevice(device_name)

        print(device_name)

        print("0. Return")

        UserInput = int(input(">>> "))
        print(deviceModule)
        if UserInput == 0:
            device_state = "menu"
        
    elif device_state == "quit":
        device_active = False
    else:
        print("UNKNOWN STATE")
        device_state = "menu"
