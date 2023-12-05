from Theremin import Theremin
import threading
import queue
import time        
import Button
import LED

class Studio:

    def __init__(self, Theremin):
        self.Theremin = Theremin
        self.dataQ = queue.Queue()

    def dataConsumer(self, dataQ, theremin):
        #this consumer gets note frequencies from the queue and plays them on the buzzer
        self.dataQ = queue.Queue()
        buttonsave = 0
        filenum = 0
        while True:
            newNote = theremin.readNote()              
            self.dataQ.put(newNote)
            toPlay = self.dataQ.get()
            if Button.read() == True or buttonsave == 1:
                buttonsave = 1
                LED.on()
                Recording.createfile()
                if Button.read() == True:
                    buttonsave = 0
                    filenum += 1
                    Recorning.save(filenum)
                    LED.off()
            if toPlay == False:
                print("Loop Broken")
                break
            else:
                theremin.playNote(toPlay)
        
    def playTheremin(self):
        threading.Thread(target = self.dataConsumer, args = (self.dataQ,self.Theremin)).start()

    def stopTheremin(self):
        self.dataQ.put(False)
