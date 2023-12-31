import pigpio
import RPi.GPIO as GPIO
import time

class Speaker:

    '''this class uses the buzzer sensors, which must be plugged into pins 12, 13, 18, or 19'''

    
    def __init__(self, SpeakerPin):
        GPIO.setmode(GPIO.BCM)
        self.SpeakerPin = SpeakerPin
        self.pi = pigpio.pi(port = 8887)


    def sing(self, Note):

        self.pi.hardware_PWM(self.SpeakerPin, Note.pitch,int(0.9*1e6))
        time.sleep(Note.duration)

    def stop(self):
        self.pi.hardware_PWM(self.SpeakerPin, 0,0 )