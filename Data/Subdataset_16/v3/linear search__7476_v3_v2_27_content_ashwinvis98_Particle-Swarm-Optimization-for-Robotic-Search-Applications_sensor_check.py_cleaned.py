import cv2
import cv2.aruco as aruco
from nxt.motor import Motor, SynchronizedMotors
from nxt.sensor import Light
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
    return nxt.locator.find_one_brick(b4 = '00:16:53:0F:0F:D8')
def fonk3(b10):
    b5 = Motor(b10, PORT_C)
    b6 = Motor(b10, PORT_A)
    b7 = Light(b10, PORT_1, False)
    b8 = {
        'b5': b5,
        'b6': b6,
        'both_motors': SynchronizedMotors(b5, b6, 0),
        'right_both_motors': SynchronizedMotors(b5, b6, 50),
        'left_both_motors': SynchronizedMotors(b6, b5, 50)
    }
    return {'b8': b8, 'b7': b7}
def fonk4(b7):
    return b7.get_input_values()[0]
def fonk5(b9, b8):
    if b9 = = 'w':
        b8['both_motors'].turn(75, 360, True)
    elif b9 = = 's':
        b8['both_motors'].turn(-75, 90, True)
    elif b9 = = 'a':
        b8['left_both_motors'].turn(75, 90, True)
    elif b9 = = 'd':
        b8['right_both_motors'].turn(75, 90, True)
def fonk6():
    b10 = fonk2()
    b11 = fonk3(b10)
    b8 = b11['b8']
    b7 = b11['b7']
    print("Ready")
    print(b10)
    b9 = ' '
    while b9 != 'q':
        b9 = fonk1()
        b12 = fonk4(b7)
        print("Light value:", b12)
        fonk5(b9, b8)
    print("Aborted!")
if b13 = = "__main__":
    fonk6()