from qr import QR
from picamera.array import PiRGBArray
from picamera import PiCamera
from time import sleep
def fonk1():
    return PiCamera()
def fonk2(b3):
    b1 = PiRGBArray(b3)
    b3.capture(b1, b2 = "bgr")
    return b1.array
def fonk3(b5, b4):
    return b4.scan(b5)
def fonk4():
    b3 = fonk1()
    b4 = QR()
    while True:
        sleep(0.5)
        b5 = fonk2(b3)
        b6 = fonk3(b5, b4)
        for f_x, f_y, data in b6:
            print(f"Coordinates: ({f_x}, {f_y}), Data: {data}")
if b7 = = "__main__":
    fonk4()