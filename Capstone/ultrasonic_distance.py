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



        
    #instance method
    def distance(self):
        ''' function returns distance reading using publically available code'''
        
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        print('first')
        if time.time() > StartTime + 1:
            return 0
        while GPIO.input(self.GPIO_ECHO) == 0:
            if time.time() > (StartTime + 1):
                return 0
            StartTime = time.time()
            
        print("second")
  
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            if time.time() > (StartTime + 2):
                return 0
            StopTime = time.time()
            
        print("Third")

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
 
        if __name__ == '__main__':
            try:
                while True:
                    dist = distance()
                    print ("Measured Distance = %.1f cm" % dist)
                    time.sleep(1)
         
                # Reset by pressing CTRL + C
            except KeyboardInterrupt:
                print("Measurement stopped by User")
                GPIO.cleanup()





