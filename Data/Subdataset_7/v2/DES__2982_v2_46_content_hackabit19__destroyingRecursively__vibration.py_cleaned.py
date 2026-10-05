import RPi.GPIO as GPIO
from time import sleep
class class1:
    def fonk1(self):
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
            left_mag, b4 = self.b3[profile]
            self.fonk2(left_mag)
            self.fonk3(b4)
        else:
            print("Unsupported Profile")
if b5 = = "__main__":
    b6 = class1()
    b6.fonk4("LEFT")
    sleep(3)
    b6.fonk4("NO CHANGE")
    GPIO.cleanup()