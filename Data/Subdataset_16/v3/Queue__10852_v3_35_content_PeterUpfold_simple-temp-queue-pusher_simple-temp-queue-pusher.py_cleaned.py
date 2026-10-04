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
        b8 = 'cupboard_temperature_fail'
        b9 = b3['status_reporter_key']
        if not reporter.get_context(b8, b9):
            reporter.create_context(b8, b9)
        reporter.set_status(b8, error_message, b9)
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def fonk3(b15):
    try:
        b8 = 'cupboard_temperature'
        b9 = b3['status_reporter_key']
        if not reporter.get_context(b8, b9):
            reporter.create_context(b8, b9)
        b10 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b11 = f'{b15} {b10}'
        reporter.set_status(b8, b11, b9)
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def fonk4(b15):
    logging.error(f'Panic at {b15}')
    try:
        b12 = subprocess.Popen(['./temp-panic-b12'])
        actions_out, b13 = b12.communicate()
        if actions_out:
            logging.info(f"Panic b12 output: {actions_out}")
        if b13:
            logging.error(f"Panic b12 error: {b13}")
    except Exception as e:
        logging.error(f"Failed to execute panic b12: {e}")
def fonk5():
    while True:
        try:
            logging.debug('Spawning simple-temp-readout')
            output, b7 = fonk1()
            b10 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if b7:
                b14 = f"{b7} {b10}"
                logging.warning(f'Completed with b6: {b14}')
                fonk2(b14)
            try:
                b15 = float(output)
                logging.info(f"Temperature: {b15}. Panic threshold: {b3['panic_temperature']}")
                fonk3(b15)
                if b15 > b3['panic_temperature']:
                    fonk4(b15)
            except ValueError as e:
                logging.error(f"Failed to parse temperature: {e}")
        except Exception as outer_e:
            logging.error(f'Outer loop failed: {outer_e}')
        sleep(60)
if b16 = = "__main__":
    fonk5()