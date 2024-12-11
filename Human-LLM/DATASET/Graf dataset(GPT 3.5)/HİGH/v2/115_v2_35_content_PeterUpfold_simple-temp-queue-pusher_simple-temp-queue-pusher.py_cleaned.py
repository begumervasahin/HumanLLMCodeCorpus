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
        b3 = ['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00']
        b4 = subprocess.Popen(b3, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, b5 = b4.communicate()
        b6 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        b7 = b5.decode('ascii').strip() + f' {b6}'
        if len(b7) > 0:
            logging.warning(f'Completed with stderr: {b7}')
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
        if len(output) > 0:
            b8 = float(output.decode('ascii').strip())
            logging.info(f"Temperature: {b8}. Panic threshold: {b1['panic_temperature']}")
            try:
                pass
            except IOError as e:
                logging.error(f'Failed to communicate with StatusReporter: {e}')
            if b8 > b1['panic_temperature']:
                logging.error(f'Panic at {b8}')
                b9 = subprocess.Popen(['./temp-panic-b9'])
                actions_out, b10 = b9.communicate()
    except Exception as outer_e:
        logging.error(f'Outer loop failed: {outer_e}')
    sleep(60)