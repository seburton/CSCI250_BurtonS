import numpy as np
import Note as Note

class Recording():
    def __init__(self, name):
        self.song = np.array([])
        self.name = name
        self.filenum = 0
    def createfile(self):
        self.song += [Note.pitch, Note.duration]
        
    def save(self):
        filename = self.name + str(self.filenum)+'.npz'
        np.save(filename, self.song)
