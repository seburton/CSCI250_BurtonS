import numpy as np
import Note as Note

class Recording():
    def __init__(self, name):
        self.song = []
        self.name = name
        self.filenum = 0
    def createfile(self, toPlay):
        self.song.append(toPlay)
        
    def save(self):
        filename = 'saves/' + self.name + str(self.filenum)
        np.save(filename, self.song)
