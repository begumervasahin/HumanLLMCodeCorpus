import yaml
import subprocess
import json
import logging
from datetime import datetime
from time import sleep
import os
import sys
b1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(b1):
    sys.path.append(b1)
from PUStatusReporter import reporter
with open('b2.yml', 'r') as config_file:
    b2 = yaml.safe_load(config_file)
logging.basicConfig(b3 = logging.INFO)
def fonk1():
    b4 = ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00']
    b5 = subprocess.Popen(b4, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, b6 = b5.communicate()
    return output, b6
def fonk2(error_message):
    try:
        if not reporter.get_context('cupboard_temperature_fail', b2['status_reporter_key']):
            reporter.create_context('cupboard_temperature_fail', b2['status_reporter_key'])
        reporter.set_status('cupboard_temperature_fail', error_message, b2['status_reporter_key'])
    except IOError as e:
        logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk3(b12):
    try:
        if not reporter.get_context('cupboard_temperature', b2['status_reporter_key']):
            reporter.create_context('cupboard_temperature', b2['status_reporter_key'])
        b7 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b8 = f'{b12} {b7}'
        reporter.set_status('cupboard_temperature', b8, b2['status_reporter_key'])
    except IOError as e:
        logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk4(b12):
    if b12 > b2['panic_temperature']:
        logging.error(f'Panic at {b12}')
        b9 = subprocess.Popen(['./temp-panic-b9'])
        actions_out, b10 = b9.communicate()
def fonk5():
    while True:
        try:
            logging.debug('Spawning simple-temp-readout b5')
            output, b6 = fonk1()
            b11 = b6.decode('ascii').strip()
            if b11:
                logging.warning(f'Completed with stderr: {b11}')
                fonk2(b11)
            try:
                b12 = float(output.decode('ascii').strip())
                logging.info(f"Temperature: {b12}. Panic threshold: {b2['panic_temperature']}")
                fonk3(b12)
                fonk4(b12)
            except Exception as e:
                logging.error(f'Failed to parse temperature output: {e}')
        except Exception as outer_e:
            logging.error(f'Outer loop failed: {outer_e}')
        sleep(60)
if b13 = = "__main__":
    fonk5()