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
    b4 = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
    b5 = Motor(b4, PORT_C)
    b6 = Motor(b4, PORT_A)
    b7 = Light(b4, PORT_1, False)
    b8 = SynchronizedMotors(b5, b6, 0)
    b9 = SynchronizedMotors(b5, b6, 50)
    b10 = SynchronizedMotors(b6, b5, 50)
    return b4, b8, b9, b10, b7
def fonk3(b4):
    print("Robot is ready to move.")
    print("Connected to:", b4)
def fonk4():
    try:
        b4, b8, b9, b10, b7 = fonk2()
        fonk3(b4)
        b11 = ''
        while b11 != 'q':
            b11 = fonk1()
            b12 = b7.get_input_values()[0]
            print("Light sensor value:", b12)
            if b11 = = 'w':
                b8.turn(75, 360, True)
            elif b11 = = 's':
                b8.turn(-75, 90, True)
            elif b11 = = 'a':
                b10.turn(75, 90, True)
            elif b11 = = 'd':
                b9.turn(75, 90, True)
        print("Movement aborted.")
    except nxt.locator.BrickNotFoundError:
        print("No LEGO Mindstorms b4 found.")
    except Exception as e:
        print(f"An error occurred: {e}")
if b13 = = "__main__":
    fonk4()