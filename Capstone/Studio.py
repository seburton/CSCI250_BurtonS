from Theremin import Theremin
import threading
import queue
import time        

class Studio:

    def __init__(self, Theremin):
        self.Theremin = Theremin
        self.dataQ = queue.Queue()

    def dataConsumer(self, dataQ, theremin):
        #this consumer gets note frequencies from the queue and plays them on the buzzer
        self.dataQ = queue.Queue()
        while True:
            newNote = theremin.readNote()              
            self.dataQ.put(newNote)
            toPlay = self.dataQ.get()
            if toPlay == False:
                print("Loop Broken")
                break
            else:
                theremin.playNote(toPlay)
        
    def playTheremin(self):
        threading.Thread(target = self.dataConsumer, args = (self.dataQ,self.Theremin)).start()

    def stopTheremin(self):
        self.dataQ.put(False)