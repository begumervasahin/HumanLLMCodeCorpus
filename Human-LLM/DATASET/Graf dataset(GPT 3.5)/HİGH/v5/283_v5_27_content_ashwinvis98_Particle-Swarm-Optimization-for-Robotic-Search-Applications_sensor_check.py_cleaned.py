import nxt.locator
import sys
import tty
import termios
from sensor.generic import *
b1 = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
b2 = Motor(b1, PORT_C)
b3 = Motor(b1, PORT_A)
b4 = Light(b1, PORT_1, False)
b5 = nxt.SynchronizedMotors(b2, b3, 0)
b6 = nxt.SynchronizedMotors(b2, b3, 50)
b7 = nxt.SynchronizedMotors(b3, b2, 50)
def fonk1():
    b8 = sys.stdin.fileno()
    b9 = termios.tcgetattr(b8)
    try:
        tty.setraw(b8)
        b10 = sys.stdin.read(1)
    finally:
        termios.tcsetattr(b8, termios.TCSADRAIN, b9)
    return b10
print("Ready")
print(b1)
b11 = ' '
while b11 != 'q':
    b11 = fonk1()
    b12 = b4.get_input_values().scaled_value
    print("Light b13 = ", b12)
    if b11 = = 'w':
        b5.turn(75, 360, True)
    elif b11 = = 's':
        b5.turn(-75, 90, True)
    elif b11 = = 'a':
        b2.turn(75, 90, True)
        b3.turn(-75, 90, True)
    elif b11 = = 'd':
        b6.turn(-75, 360, True)
print("Aborted!")