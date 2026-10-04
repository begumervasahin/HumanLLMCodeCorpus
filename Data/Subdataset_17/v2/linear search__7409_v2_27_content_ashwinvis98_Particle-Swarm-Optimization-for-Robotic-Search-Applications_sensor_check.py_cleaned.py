import cv2
import cv2.aruco as aruco
from nxt.motor import *
from nxt.sensor import *
import tty
import sys
import termios
import nxt.locator
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
def main():
    brick = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
    left_motor = Motor(brick, PORT_C)
    right_motor = Motor(brick, PORT_A)
    light_sensor = Light(brick, PORT_1, False)
    both_motors = SynchronizedMotors(left_motor, right_motor, 0)
    right_both_motors = SynchronizedMotors(left_motor, right_motor, 50)
    left_both_motors = SynchronizedMotors(right_motor, left_motor, 50)
    print("Ready")
    print(brick)
    user_input = ' '
    while user_input != 'q':
        user_input = getch()
        light_value = light_sensor.get_input_values()[0]
        print("Light value:", light_value)
        if user_input == 'w':
            both_motors.turn(75, 360, True)
        elif user_input == 's':
            both_motors.turn(-75, 90, True)
        elif user_input == 'a':
            left_both_motors.turn(75, 90, True)
        elif user_input == 'd':
            right_both_motors.turn(75, 90, True)
    print("Aborted!")
if __name__ == "__main__":
    main()