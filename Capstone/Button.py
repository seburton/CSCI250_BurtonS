import RPi.GPIO as GPIO

class Button():
    def __init__(self, buttonPin):
        GPIO.setmode(GPIO.BCM)
        self.buttonPin = buttonPin
        
    def read(self):
        GPIO.setup(self.buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        buttonbool = GPIO.input(self.buttonPin)
        return buttonbool