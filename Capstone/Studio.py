from Theremin import Theremin
import threading
import queue
import time        
import Button
import LED
import Recording

class Studio:

    def __init__(self, Theremin, Button, Light, Recording, Button, Light):
        self.Theremin = Theremin
        self.Button = Button
        self.Light = Light
        self.Recording = Recording
        self.dataQ = queue.Queue()

    def dataConsumer(self, dataQ, theremin, recording, button, light):
        #this consumer gets note frequencies from the queue and plays them on the buzzer
        self.dataQ = queue.Queue()
        buttonsave = 0
        while True:
            newNote = theremin.readNote()              
            self.dataQ.put(newNote)
            toPlay = self.dataQ.get()
            if button.read() == True or buttonsave == 1:
                buttonsave = 1
                light.on()
                recording.createfile()
                if button.read() == True:
                    buttonsave = 0
                    recording.filenum += 1
                    recording.save()
                    light.off()
            if toPlay == False:
                print("Loop Broken")
                break
            else:
                theremin.playNote(toPlay)
        
    def playTheremin(self):
        threading.Thread(target = self.dataConsumer, args = (self.dataQ,self.Theremin, self.Recording, self.Button, Self.Light)).start()

    def stopTheremin(self):
        self.dataQ.put(False)
