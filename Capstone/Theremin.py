import DistanceSensor
from Speaker import Speaker
from Note import Note
import threading

class Theremin:
    
    def __init__(self, noteSensor, typeSensor, leftSpeaker, rightSpeaker):
        self.noteSensor = noteSensor
        self.typeSensor = typeSensor
        self.leftSpeaker = leftSpeaker
        self.rightSpeaker = rightSpeaker
        
    def playNote(self, note):
        leftThread = threading.Thread(target = self.leftSpeaker.sing, args=(note,))
        rightThread = threading.Thread(target = self.rightSpeaker.sing, args=(note,))

        leftThread.start()
        rightThread.start()

    
    def readNote(self):
        distances = []
        for i in range(5):
            noteDistance = self.noteSensor.read()
            distances.append(noteDistance)
        type = self.readType()
        newNote = Note(distances, type)
        
        return newNote

    def readType(self):
        type = []
        for i in range(5):
            noteType = self.typeSensor.read()
            type.append(noteType)
        
        return type