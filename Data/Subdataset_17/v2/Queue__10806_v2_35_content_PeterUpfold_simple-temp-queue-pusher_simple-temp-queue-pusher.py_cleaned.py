import yaml
import subprocess
import json
import logging
from datetime import datetime
from time import sleep
import os
import sys
logging.basicConfig(level=logging.INFO)
libdir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
from PUStatusReporter import reporter
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
def read_temperature():
    try:
        proc = subprocess.Popen(
            ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output, err = proc.communicate()
        return output.decode('ascii').strip(), err.decode('ascii').strip()
    except Exception as e:
        logging.error(f"Failed to read temperature: {e}")
        return None, str(e)
def report_error(error_message):
    try:
        if not reporter.get_context('cupboard_temperature_fail', config['status_reporter_key']):
            reporter.create_context('cupboard_temperature_fail', config['status_reporter_key'])
        reporter.set_status('cupboard_temperature_fail', error_message, config['status_reporter_key'])
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def report_temperature(actual_temp):
    try:
        if not reporter.get_context('cupboard_temperature', config['status_reporter_key']):
            reporter.create_context('cupboard_temperature', config['status_reporter_key'])
        date_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        actual_temp_with_date = f'{actual_temp} {date_string}'
        reporter.set_status('cupboard_temperature', actual_temp_with_date, config['status_reporter_key'])
    except IOError as e:
        logging.error(f"Failed to communicate with StatusReporter: {e}")
def handle_panic(actual_temp):
    logging.error(f'Panic at {actual_temp}')
    try:
        actions = subprocess.Popen(['./temp-panic-actions'])
        actions_out, actions_err = actions.communicate()
        if actions_out:
            logging.info(f"Panic actions output: {actions_out}")
        if actions_err:
            logging.error(f"Panic actions error: {actions_err}")
    except Exception as e:
        logging.error(f"Failed to execute panic actions: {e}")
def main_loop():
    while True:
        try:
            logging.debug('Spawning simple-temp-readout')
            output, err = read_temperature()
            date_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if err:
                err_message = f"{err} {date_string}"
                logging.warning(f'Completed with stderr: {err_message}')
                report_error(err_message)
            try:
                actual_temp = float(output)
                logging.info(f"Temperature: {actual_temp}. Panic threshold: {config['panic_temperature']}")
                report_temperature(actual_temp)
                if actual_temp > config['panic_temperature']:
                    handle_panic(actual_temp)
            except ValueError as e:
                logging.error(f"Failed to parse temperature: {e}")
        except Exception as outer_e:
            logging.error(f'Outer loop failed: {outer_e}')
        sleep(60)
if __name__ == "__main__":
    main_loop()