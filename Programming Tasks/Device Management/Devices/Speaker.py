import _BaseDevice as Parent

class Speaker(Parent):
    def __init__(self):
        self.device_type = "Speaker"

        self.volume = 0
        self.song = "dua lipa"

    def change_volume(self,newvolume):
        self.volume = newvolume

    def change_song(self,newsong):
        self.song = newsong
