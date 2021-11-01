from abc import ABC

class SmartDevice(ABC):
    wifi_password = "ALC"

    def connect_wifi(self):
        pass

    def power_on(self):
        pass

    def power_off(self):
        pass
