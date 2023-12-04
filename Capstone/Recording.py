import numpy as np
import Note as Note

class Recording():
    def __init__(self, name):
        self.song = np.array([])
        self.name = name
        
    def createfile(self):
        self.song += [Note.pitch, Note.duration]
        
    def save(self):
        np.save(self.name, self.song)
