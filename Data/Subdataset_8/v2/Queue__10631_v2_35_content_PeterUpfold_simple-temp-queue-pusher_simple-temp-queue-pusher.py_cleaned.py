import yaml
import subprocess
import logging
from datetime import datetime
from time import sleep
with open('config.yml', 'r') as config_file:
    config = yaml.safe_load(config_file)
logging.basicConfig(level=logging.INFO)
while True:
    try:
        logging.debug('Spawning simple-temp-readout subprocess')
        cmd = ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00']
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, err = proc.communicate()
        date_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        err_string = err.decode('ascii').strip() + f' {date_string}'
        if len(err_string) > 0:
            logging.warning(f'Completed with stderr: {err_string}')
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
        if len(output) > 0:
            actual_temp = float(output.decode('ascii').strip())
            logging.info(f"Temperature: {actual_temp}. Panic threshold: {config['panic_temperature']}")
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
            if actual_temp > config['panic_temperature']:
                logging.error(f'Panic at {actual_temp}')
                actions = subprocess.Popen(['./temp-panic-actions'])
                actions_out, actions_err = actions.communicate()
    except Exception as outer_e:
        logging.error(f'Outer loop failed: {outer_e}')
    sleep(60)