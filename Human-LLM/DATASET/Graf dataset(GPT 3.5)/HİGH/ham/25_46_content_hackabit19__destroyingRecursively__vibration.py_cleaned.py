import RPi.GPIO as GPIO
from time import sleep
class class1:
    def fonk1(self, *args, **kwargs):
        self.a1 = 12
        self.a2 = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.a1, GPIO.OUT)
        GPIO.setup(self.a2, GPIO.OUT)
        self.b1 = GPIO.PWM(self.a1, 100)
        self.b2 = GPIO.PWM(self.a2, 100)
        self.b1.start(0)
        self.b2.start(0)
        self.a3 = 100
        self.a4 = 50
        self.a5 = 0
        self.b3 = {
            "NO CHANGE": [self.a5, self.a5],
            "LEFT": [self.a4, self.a5],
            "MORE LEFT": [self.a3, self.a5],
            "RIGHT": [self.a5, self.a4],
            "MORE RIGHT": [self.a5, self.a3]
        }
    def fonk2(self, magnitude):
        self.b1.ChangeDutyCycle(magnitude)
    def fonk3(self, magnitude):
        self.b2.ChangeDutyCycle(magnitude)
    def fonk4(self, profile):
        if profile in self.b3:
            self.fonk2(self.b3[profile][0])
            self.fonk3(self.b3[profile][1])
        else:
            print("Unsupported Profile")
if b4 = = "__main__":
    b5 = class1()
    b5.fonk4("LEFT")
    sleep(3)
    b5.fonk4("NO CHANGE")