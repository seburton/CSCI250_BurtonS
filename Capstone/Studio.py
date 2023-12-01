from Theremin import Theremin
import threading
import queue
import time

def dataProducer(dataQ, theremin, playing):
    #This producer collects data from the distance sensor and adds note frequencies to the queue
    newNote = theremin.readNote()
                
            
    dataQ.put(newNote)

def dataConsumer(dataQ, theremin):
    #this consumer gets note frequencies from the queue and plays them on the buzzer
    toPlay = dataQ.get()
    theremin.playNote(toPlay)

class Studio:

    def __init__(self, Theremin):
        self.Theremin = Theremin
        self.dataQ = queue.Queue()
        self.dataCollection = threading.Thread(target = dataProducer, args = (self.dataQ,self.Theremin))
        self.dataReading = threading.Thread(target = dataConsumer, args = (self.dataQ,self.Theremin))
        
        
    def playTheremin(self, playing):
        if playing == True:
            self.dataCollection.start()
            self.dataReading.start()
            
            dataQ.join()

        if playing == False:
            stop_threads = True