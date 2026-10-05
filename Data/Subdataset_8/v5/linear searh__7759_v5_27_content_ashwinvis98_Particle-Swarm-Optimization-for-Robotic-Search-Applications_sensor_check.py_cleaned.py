import nxt.locator
import sys
import tty
import termios
from sensor.generic import *
brick = nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
left_motor = Motor(brick, PORT_C)
right_motor = Motor(brick, PORT_A)
light_sensor = Light(brick, PORT_1, False)
both_motors = nxt.SynchronizedMotors(left_motor, right_motor, 0)
right_motor_sync = nxt.SynchronizedMotors(left_motor, right_motor, 50)
left_motor_sync = nxt.SynchronizedMotors(right_motor, left_motor, 50)
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        char = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return char
print("Ready")
print(brick)
user_input = ' '
while user_input != 'q':
    user_input = getch()
    light_value = light_sensor.get_input_values().scaled_value
    print("Light value =", light_value)
    if user_input == 'w':
        both_motors.turn(75, 360, True)
    elif user_input == 's':
        both_motors.turn(-75, 90, True)
    elif user_input == 'a':
        left_motor.turn(75, 90, True)
        right_motor.turn(-75, 90, True)
    elif user_input == 'd':
        right_motor_sync.turn(-75, 360, True)
print("Aborted!")