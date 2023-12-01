from Theremin import Theremin
import threading
import queue
import time

def dataProducer(dataQ, theremin, playing):
    #This producer collects data from the distance sensor and adds note frequencies to the queue
    while playing == True:
        newNote = theremin.readNote()              
        dataQ.put(newNote)
        if end == True:
            playing = False

def dataConsumer(dataQ, theremin, playing):
    #this consumer gets note frequencies from the queue and plays them on the buzzer
    global end
    end = False
    startTime = time.time()
    while playing == True:
        toPlay = dataQ.get()
        if time.time() > startTime + 5:
            dataQ.put(True)
        if isinstnace(toPlay, bool):
            playing = False
            end = True
            
        else:
            theremin.playNote(toPlay)
        

class Studio:

    def __init__(self, Theremin):
        self.Theremin = Theremin
        self.dataQ = queue.Queue()
        self.dataCollection = threading.Thread(target = dataProducer, args = (self.dataQ,self.Theremin, self.Theremin.readType()))
        self.dataReading = threading.Thread(target = dataConsumer, args = (self.dataQ,self.Theremin, self.Theremin.readType()))
        
        
    def playTheremin(self, playing):
        if playing == True:
            self.dataCollection.start()
            self.dataReading.start()
            
            self.dataQ.join()
            