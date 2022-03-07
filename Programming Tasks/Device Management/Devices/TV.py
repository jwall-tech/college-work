import _BaseDevice as Parent

class TV(Parent):
    def __init__(self):
        self.device_type = "Television"

        self.volume = 0
        self.playing = "dua lipa"

    def change_volume(self,newvolume):
        self.volume = newvolume

    def change_song(self,playing):
        self.playing = playing
