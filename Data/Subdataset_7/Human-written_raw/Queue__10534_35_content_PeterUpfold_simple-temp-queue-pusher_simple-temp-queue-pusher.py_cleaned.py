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
b2 = open('b3.yml', 'r')
b3 = yaml.safe_load(b2)
logging.basicConfig(b4 = logging.INFO)
while True:
	try:
		logging.debug('Spawning simple-temp-readout')
		b5 = subprocess.Popen(['./simple-temp-readout', '/dev/hidraw1', '0x01', '0x80', '0x33', '0x01', '0x00', '0x00', '0x00', '0x00'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		output, b6 = b5.communicate()
		b7 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		b8 = b6.decode('ascii').strip() + f' {b7}'
		if len(b8) > 0:
			logging.warning(f'Completed with stderr: {b8}')
			try:
				if not reporter.get_context('cupboard_temperature_fail', b3['status_reporter_key']):
					reporter.create_context('cupboard_temperature_fail', b3['status_reporter_key'])
				reporter.set_status('cupboard_temperature_fail', b8, b3['status_reporter_key'])
			except IOError as e:
				logging.error(f'Failed to communicate with StatusReporter: {e}')
		try:
			b9 = float(output.decode('ascii').strip())
			logging.info(f"Temperature: {b9}. Panic threshold: {b3['panic_temperature']}")
			try:
				if not reporter.get_context('cupboard_temperature', b3['status_reporter_key']):
					reporter.create_context('cupboard_temperature', b3['status_reporter_key'])
				b7 = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				b10 = f'{b9} {b7}'
				reporter.set_status('cupboard_temperature', b10, b3['status_reporter_key'])
			except IOError as e:
				logging.error(f'Failed to communicate with StatusReporter: {e}')
			if b9 > b3['panic_temperature']:
				logging.error(f'Panic at {b9}')
				b11 = subprocess.Popen(['./temp-panic-b11'])
				actions_out, b12 = b11.communicate()
		except Exception as e:
			logging.error(f'parse fail? {e}')
		if len(output) > 0:
			pass
	except Exception as outer_e:
		logging.error(f'Outer loop failed: {outer_e}')
	sleep(60)