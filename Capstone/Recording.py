import numpy as np
import Note as Note

class Recording():
    def __init__(self, name):
        self.song = []
        self.name = name
        self.filenum = 0
    def createfile(self, toplay):
        self.song.append(toplay)
        
    def save(self):
        filename = 'saves/' + self.name + str(self.filenum)
        np.savez(filename, self.song)
