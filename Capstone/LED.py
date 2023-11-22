import RPi.GPIO as GPIO

class LED():
    def __init__(self,ledPin):
        GPIO.setmode(GPIO.BCM)
        self.ledPin = ledPin

    def on(self):      
        GPIO.setup(self.ledPin, GPIO.OUT)
        GPIO.output(self.ledPin, True)
        

    def off(self):
        GPIO.output(self.ledPin, False)