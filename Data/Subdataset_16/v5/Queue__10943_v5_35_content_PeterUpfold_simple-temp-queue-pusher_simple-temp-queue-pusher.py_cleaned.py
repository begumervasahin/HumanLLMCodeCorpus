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
def fonk1(config_file_path):
    with open(config_file_path, 'r') as config_file:
        return yaml.safe_load(config_file)
b2 = fonk1('b2.yml')
logging.basicConfig(b3 = logging.INFO)
def fonk2():
    b4 = ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00']
    b5 = subprocess.Popen(b4, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, b6 = b5.communicate()
    return output, b6
def fonk3(b6, b12):
    b7 = b6.decode('ascii').strip() + f' {b12}'
    if b7:
        logging.warning(f'Completed with stderr: {b7}')
        try:
            b8 = 'cupboard_temperature_fail'
            if not reporter.get_context(b8, b2['status_reporter_key']):
                reporter.create_context(b8, b2['status_reporter_key'])
            reporter.set_status(b8, b7, b2['status_reporter_key'])
        except IOError as e:
            logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk4(b13, b12):
    logging.info(f"Temperature: {b13}. Panic threshold: {b2['panic_temperature']}")
    try:
        b8 = 'cupboard_temperature'
        if not reporter.get_context(b8, b2['status_reporter_key']):
            reporter.create_context(b8, b2['status_reporter_key'])
        b9 = f'{b13} {b12}'
        reporter.set_status(b8, b9, b2['status_reporter_key'])
    except IOError as e:
        logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk5(b13):
    logging.error(f'Panic at {b13}')
    b10 = subprocess.Popen(['./temp-panic-b10'])
    actions_out, b11 = b10.communicate()
def fonk6():
    while True:
        try:
            logging.debug('Spawning simple-temp-readout')
            output, b6 = fonk2()
            b12 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if b6:
                fonk3(b6, b12)
            try:
                b13 = float(output.decode('ascii').strip())
                fonk4(b13, b12)
                if b13 > b2['panic_temperature']:
                    fonk5(b13)
            except ValueError as e:
                logging.error(f'Failed to parse temperature: {e}')
        except Exception as outer_e:
            logging.error(f'Outer loop failed: {outer_e}')
        sleep(60)
if b14 = = '__main__':
    fonk6()