import yaml
import subprocess
import logging
from datetime import datetime
from time import sleep
with open('b1.yml', 'r') as config_file:
    b1 = yaml.safe_load(config_file)
logging.basicConfig(b2 = logging.INFO)
while True:
    try:
        logging.debug('Spawning simple-temp-readout subprocess')
        b3 = subprocess.Popen(['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, b4 = b3.communicate()
        b5 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b6 = b4.decode('ascii').strip() + f' {b5}'
        if len(b6) > 0:
            logging.warning(f'Completed with stderr: {b6}')
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
        if len(output) > 0:
            b7 = float(output.decode('ascii').strip())
            logging.info(f"Temperature: {b7}. Panic threshold: {b1['panic_temperature']}")
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
            if b7 > b1['panic_temperature']:
                logging.error(f'Panic at {b7}')
                b8 = subprocess.Popen(['./temp-panic-b8'])
                actions_out, b9 = b8.communicate()
    except Exception as outer_e:
        logging.error(f'Outer loop failed: {outer_e}')
    sleep(60)