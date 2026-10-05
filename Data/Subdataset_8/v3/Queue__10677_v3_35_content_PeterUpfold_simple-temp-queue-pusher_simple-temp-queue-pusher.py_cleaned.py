import yaml
import subprocess
import logging
from datetime import datetime
from time import sleep
def load_configuration(file_path):
    with open(file_path, 'r') as config_file:
        return yaml.safe_load(config_file)
def run_simple_temp_readout(cmd):
    try:
        return subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    except Exception as e:
        logging.error(f'Failed to execute simple-temp-readout: {e}')
        return b'', b''
def report_status(message):
    try:
        pass
    except IOError as e:
        logging.error(f'Failed to communicate with StatusReporter: {e}')
def execute_panic_actions(cmd):
    try:
        subprocess.Popen(cmd).communicate()
    except Exception as e:
        logging.error(f'Failed to execute panic actions: {e}')
def main(config):
    while True:
        try:
            logging.debug('Spawning simple-temp-readout subprocess')
            output, err = run_simple_temp_readout(config['simple_temp_readout_cmd'])
            date_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            err_string = err.decode('ascii').strip() + f' {date_string}'
            if len(err_string) > 0:
                logging.warning(f'Completed with stderr: {err_string}')
                report_status(err_string)
            if len(output) > 0:
                actual_temp = float(output.decode('ascii').strip())
                logging.info(f"Temperature: {actual_temp}. Panic threshold: {config['panic_temperature']}")
                report_status(actual_temp)
                if actual_temp > config['panic_temperature']:
                    logging.error(f'Panic at {actual_temp}')
                    execute_panic_actions(config['panic_actions_cmd'])
        except Exception as e:
            logging.error(f'Outer loop failed: {e}')
        sleep(config['loop_interval'])
if __name__ == "__main__":
    config = load_configuration('config.yml')
    logging.basicConfig(level=logging.INFO)
    main(config)