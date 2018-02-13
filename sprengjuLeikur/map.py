from sprengjuLeikur.settings import *
class Map:
    def __init__(self, file):
        self.map_data = []

        with open(file, "rt") as f:
            for line in f:
                self.map_data.append(line.strip())
        self.tilewidth = len(self.map_data[0])
        self.tileheight = len(self.map_data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE
