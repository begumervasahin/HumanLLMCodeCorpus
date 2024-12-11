import cv2
import cv2.aruco as aruco
from nxt.motor import *
from nxt.sensor import *
import tty
import sys
import termios
import nxt.locator
def fonk1():
    b1 = sys.stdin.fileno()
    b2 = termios.tcgetattr(b1)
    try:
        tty.setraw(b1)
        b3 = sys.stdin.read(1)
    finally:
        termios.tcsetattr(b1, termios.TCSADRAIN, b2)
    return b3
def fonk2():
    b4 = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
    b5 = Motor(b4, PORT_C)
    b6 = Motor(b4, PORT_A)
    b7 = Light(b4, PORT_1, False)
    b8 = SynchronizedMotors(b5, b6, 0)
    b9 = SynchronizedMotors(b5, b6, 50)
    b10 = SynchronizedMotors(b6, b5, 50)
    print("Ready")
    print(b4)
    b3 = ' '
    while b3 != 'q':
        b3 = fonk1()
        b11 = b7.get_input_values()[0]
        print("Light value:", b11)
        if b3 = = 'w':
            b8.turn(75, 360, True)
        elif b3 = = 's':
            b8.turn(-75, 90, True)
        elif b3 = = 'a':
            b10.turn(75, 90, True)
        elif b3 = = 'd':
            b9.turn(75, 90, True)
    print("Aborted!")
if b12 = = "__main__":
    fonk2()