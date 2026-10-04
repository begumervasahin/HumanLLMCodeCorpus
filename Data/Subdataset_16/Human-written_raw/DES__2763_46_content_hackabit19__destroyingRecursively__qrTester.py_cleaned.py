from b2 import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
import cv2
b1 = PiCamera()
b2 = QR()
while True:
    sleep(0.5)
    b3 = PiRGBArray(b1)
    b1.capture(b3, "bgr")
    b4 = b3.array
    for f_x, f_y, data in b2.scan(b4):
        print(f_x, f_y, data)