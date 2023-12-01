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
        for i in range(10):
            noteDistance = self.noteSensor.read()
            distances.append(noteDistance)
        newNote = Note(distances)
        
        return newNote