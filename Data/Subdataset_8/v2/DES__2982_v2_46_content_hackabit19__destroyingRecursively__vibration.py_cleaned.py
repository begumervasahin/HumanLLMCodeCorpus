import RPi.GPIO as GPIO
from time import sleep
class Vibrators:
    def __init__(self):
        self.left_pin = 12
        self.right_pin = 13
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_pin, GPIO.OUT)
        GPIO.setup(self.right_pin, GPIO.OUT)
        self.left_pwm = GPIO.PWM(self.left_pin, 100)
        self.right_pwm = GPIO.PWM(self.right_pin, 100)
        self.left_pwm.start(0)
        self.right_pwm.start(0)
        self.HIGH = 100
        self.MID = 50
        self.OFF = 0
        self.profiles = {
            "NO CHANGE": [self.OFF, self.OFF],
            "LEFT": [self.MID, self.OFF],
            "MORE LEFT": [self.HIGH, self.OFF],
            "RIGHT": [self.OFF, self.MID],
            "MORE RIGHT": [self.OFF, self.HIGH]
        }
    def set_left_vibration(self, magnitude):
        self.left_pwm.ChangeDutyCycle(magnitude)
    def set_right_vibration(self, magnitude):
        self.right_pwm.ChangeDutyCycle(magnitude)
    def set_profile(self, profile):
        if profile in self.profiles:
            left_mag, right_mag = self.profiles[profile]
            self.set_left_vibration(left_mag)
            self.set_right_vibration(right_mag)
        else:
            print("Unsupported Profile")
if __name__ == "__main__":
    vibrators = Vibrators()
    vibrators.set_profile("LEFT")
    sleep(3)
    vibrators.set_profile("NO CHANGE")
    GPIO.cleanup()