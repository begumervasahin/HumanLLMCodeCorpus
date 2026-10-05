import nxt.locator
import sys
import cv2
import cv2.aruco as aruco
from sensor.generic import *
import tty, termios
from nxt.motor import *
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
b10 = ' '
print ("Ready")
print (b1)
while b10 != 'q':
	b10 = fonk1()
	b11 = b4.get_input_values().scaled_value
	print("b12 = ",b11)
	if b10 = = 'w':
		b5.turn(75, 360, True)
	elif b10 = = 's':
		b5.turn(-75, 90, True)
	elif b10 = = 'a':
		b2.turn(75, 90, True)
		b3.turn(-75, 90, True)
	elif b10 = = 'd':
		b6.turn(-75, 360, True)
print ("Aborted!")