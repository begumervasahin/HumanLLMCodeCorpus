import cv2
import cv2.aruco as aruco
from nxt.motor import Motor, SynchronizedMotors
from nxt.sensor import Light
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
def initialize_brick():
    return nxt.locator.find_one_brick(host='00:16:53:0F:0F:D8')
def initialize_motors_and_sensors(brick):
    left_motor = Motor(brick, PORT_C)
    right_motor = Motor(brick, PORT_A)
    light_sensor = Light(brick, PORT_1, False)
    motors = {
        'left_motor': left_motor,
        'right_motor': right_motor,
        'both_motors': SynchronizedMotors(left_motor, right_motor, 0),
        'right_both_motors': SynchronizedMotors(left_motor, right_motor, 50),
        'left_both_motors': SynchronizedMotors(right_motor, left_motor, 50)
    }
    return {'motors': motors, 'light_sensor': light_sensor}
def read_light_sensor(light_sensor):
    return light_sensor.get_input_values()[0]
def execute_user_command(user_input, motors):
    if user_input == 'w':
        motors['both_motors'].turn(75, 360, True)
    elif user_input == 's':
        motors['both_motors'].turn(-75, 90, True)
    elif user_input == 'a':
        motors['left_both_motors'].turn(75, 90, True)
    elif user_input == 'd':
        motors['right_both_motors'].turn(75, 90, True)
def control_robot():
    brick = initialize_brick()
    components = initialize_motors_and_sensors(brick)
    motors = components['motors']
    light_sensor = components['light_sensor']
    print("Ready")
    print(brick)
    user_input = ' '
    while user_input != 'q':
        user_input = getch()
        light_value = read_light_sensor(light_sensor)
        print("Light value:", light_value)
        execute_user_command(user_input, motors)
    print("Aborted!")
if __name__ == "__main__":
    control_robot()