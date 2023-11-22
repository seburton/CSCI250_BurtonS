#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
#GPIO.setmode(GPIO.BCM)

class DistanceSensor:
    "class Distance describes distance sensor. Initialize with arguments, trigPin, echoPin."

    def __init__(self, trig, echo):
        GPIO.setmode(GPIO.BCM)
        self.GPIO_TRIGGER = trig
        self.GPIO_ECHO = echo

        
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)


    


        
    #instance method
    def read(self):
        ''' function returns distance reading using publically available code'''
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)   
        
        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
            
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        time.sleep(0.05)

        return distance
 




