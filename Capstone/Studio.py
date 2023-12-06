from Theremin import Theremin
import threading
import queue
import time        
import Button
import LED
import Recording

class Studio:

    def __init__(self, Theremin, Button, Light, Recording):
        self.Theremin = Theremin
        self.Button = Button
        self.Light = Light
        self.Recording = Recording
        self.dataQ = queue.Queue()

    def dataConsumer(self, dataQ, theremin, button, light, recording, ):
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
                recording.createfile(toPlay)
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
        threading.Thread(target = self.dataConsumer, args = (self.dataQ,self.Theremin, self.Button, self.Light, self.Recording)).start()

    def stopTheremin(self):
        self.dataQ.put(False)

    def playback(self, filename):
        data = np.load(filename, allow_pickle = True)
        for i in data.pitch:
            self.Theremin.playNote(i)


