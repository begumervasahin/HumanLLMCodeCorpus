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
b2 = 'b3.yml'
with open(b2, 'r') as config_file:
    b3 = yaml.safe_load(config_file)
logging.basicConfig(b4 = logging.INFO)
def fonk1():
    b5 = ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00']
    b6 = subprocess.Popen(b5, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, b7 = b6.communicate()
    return output, b7
def fonk2(b7, b12):
    b8 = b7.decode('ascii').strip() + f' {b12}'
    if b8:
        logging.warning(f'Completed with stderr: {b8}')
        try:
            if not reporter.get_context('cupboard_temperature_fail', b3['status_reporter_key']):
                reporter.create_context('cupboard_temperature_fail', b3['status_reporter_key'])
            reporter.set_status('cupboard_temperature_fail', b8, b3['status_reporter_key'])
        except IOError as e:
            logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk3(b13, b12):
    logging.info(f"Temperature: {b13}. Panic threshold: {b3['panic_temperature']}")
    try:
        if not reporter.get_context('cupboard_temperature', b3['status_reporter_key']):
            reporter.create_context('cupboard_temperature', b3['status_reporter_key'])
        b9 = f'{b13} {b12}'
        reporter.set_status('cupboard_temperature', b9, b3['status_reporter_key'])
    except IOError as e:
        logging.error(f'Failed to communicate with StatusReporter: {e}')
def fonk4(b13):
    logging.error(f'Panic at {b13}')
    b10 = subprocess.Popen(['./temp-panic-b10'])
    actions_out, b11 = b10.communicate()
while True:
    try:
        logging.debug('Spawning simple-temp-readout')
        output, b7 = fonk1()
        b12 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if b7:
            fonk2(b7, b12)
        try:
            b13 = float(output.decode('ascii').strip())
            fonk3(b13, b12)
            if b13 > b3['panic_temperature']:
                fonk4(b13)
        except ValueError as e:
            logging.error(f'Failed to parse temperature: {e}')
    except Exception as outer_e:
        logging.error(f'Outer loop failed: {outer_e}')
    sleep(60)