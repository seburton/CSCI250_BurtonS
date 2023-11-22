import pigpio
import RPi.GPIO as GPIO
import time

class Speaker:

    '''this class uses the buzzer sensors, which must be plugged into pins 12, 13, 18, or 19'''

    
    def __init__(self, SpeakerPin):
        GPIO.setmode(GPIO.BCM)
        self.SpeakerPin = SpeakerPin

    def sing(self, Note):
        pi = pigpio.pi(port = 8887)

        print(Note.pitch)
        pi.hardware_PWM(self.SpeakerPin, Note.pitch,int(1e6))
        time.sleep(Note.duration)
        pi.hardware_PWM(self.SpeakerPin, 0,0 )