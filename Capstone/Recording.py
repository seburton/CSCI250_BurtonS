import numpy as np
import Note as Note

class Recording():
    def __init__(self, name):
        self.song = np.array([])
        self.name = name
        self.filenum = 0
    def createfile(self):
        self.song += toplay
        
    def save(self):
        filename = 'saves/' + self.name + str(self.filenum)+'.npz'
        np.save(filename, self.song)
