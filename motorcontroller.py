import importlib.util
try: 
	# Check and import real RPi.GPIO library
    importlib.util.find_spec('RPi.GPIO')
    import RPi.GPIO as GPIO
except ImportError:
	# If real RPi.GPIO library fails, load the fake one
    import FakeRPi.GPIO as GPIO

class MotorController(object):
    def __init__(self):
        self.PWMA1 = 6 
        self.PWMA2 = 13
        self.D1 = 12
        self.PWM = 50
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.PWMA1,GPIO.OUT)
        GPIO.setup(self.PWMA2,GPIO.OUT)
        GPIO.setup(self.D1,GPIO.OUT)

        self.p1 = GPIO.PWM(self.D1,500)
        if (self.p1 != None) :
            self.p1.start(self.PWM)

    def	set_motor(self, A1,A2):
        GPIO.output(self.PWMA1,A1)
        GPIO.output(self.PWMA2,A2)

    def turnLeft(self):
        self.set_motor(1,0)

    def turnRight(self):
        self.set_motor(0,1)    

    def stop(self):
        self.set_motor(0,0)  

    def faster(self):
        if (self.PWM + 10 < 101):
            self.PWM = self.PWM + 10
            if (self.p1 != None) :
                self.p1.ChangeDutyCycle(self.PWM)

    def slower(self):
        if (self.PWM - 10 > -1):
            self.PWM = self.PWM - 10
            if (self.p1 != None) :
                self.p1.ChangeDutyCycle(self.PWM)    