import yaml
import subprocess
import json
import logging
from datetime import datetime
from time import sleep
import os
import sys
logging.basicConfig(b1 = logging.INFO)
b2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(b2):
    sys.path.append(b2)
from PUStatusReporter import reporter
with open('b3.yml', 'r') as config_file:
    b3 = yaml.safe_load(config_file)
def fonk1():
    try:
        b4 = subprocess.Popen(
            ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00'],
            b5 = subprocess.PIPE,
            b6 = subprocess.PIPE
        )
        output, b7 = b4.communicate()
        return output.decode('ascii').strip(), b7.decode('ascii').strip()
    except Exception as e:
        logging.error(f"Failed to read temperature: {e}")
        return None, str(e)
def fonk2(error_message):
    try:
        if not reporter.get_context('cupboard_temperature_fail', b3['status_reporter_key']):
            reporter.create_context('cupboard_temperature_fail', b3['status_reporter_key'])
        reporter.set_status('cupboard_temperature_fail', error_message, b3['status_reporter_key'])
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def fonk3(b13):
    try:
        if not reporter.get_context('cupboard_temperature', b3['status_reporter_key']):
            reporter.create_context('cupboard_temperature', b3['status_reporter_key'])
        b8 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b9 = f'{b13} {b8}'
        reporter.set_status('cupboard_temperature', b9, b3['status_reporter_key'])
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def fonk4(b13):
    logging.error(f'Panic at {b13}')
    try:
        b10 = subprocess.Popen(['./temp-panic-b10'])
        actions_out, b11 = b10.communicate()
    except Exception as e:
        logging.error(f"Failed to execute panic b10: {e}")
while True:
    try:
        logging.debug('Spawning simple-temp-readout')
        output, b7 = fonk1()
        b8 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if b7:
            b12 = f"{b7} {b8}"
            logging.warning(f'Completed with b6: {b12}')
            fonk2(b12)
        try:
            b13 = float(output)
            logging.info(f"Temperature: {b13}. Panic threshold: {b3['panic_temperature']}")
            fonk3(b13)
            if b13 > b3['panic_temperature']:
                fonk4(b13)
        except ValueError as e:
            logging.error(f"Failed to parse temperature: {e}")
    except Exception as outer_e:
        logging.error(f'Outer loop failed: {outer_e}')
    sleep(60)