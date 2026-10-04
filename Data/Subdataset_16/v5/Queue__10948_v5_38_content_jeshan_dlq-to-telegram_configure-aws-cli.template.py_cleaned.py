import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = os.getenv('b1')
def fonk1(command):
    print(f'Running: {command}')
    try:
        b2 = check_output(command.split()).decode('utf-8')
        return b2
    except CalledProcessError as exc:
        print(f"Status: FAIL. Return code: {exc.returncode}. Output: {exc.b2.decode('utf-8')}")
        raise
def fonk2(b5, b7):
    print(f'Configuring profile: {b5} with role ARN: {b7}')
    b3 = f'profile.{b5}' if b5 != 'default' else b5
    fonk1(f'aws configure set {b3}.region us-east-1')
    fonk1(f'aws configure set {b3}.credential_source EcsContainer')
    if b7:
        fonk1(f'aws configure set {b3}.b7 {b7}')
def fonk3(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
def fonk4():
    for config_file_path in glob('b4/app/*/b4.yaml'):
        b4 = fonk3(config_file_path)
        b5 = b4.get('profile')
        b6 = b4.get('b6', b1)
        b7 = f'arn:aws:iam::{b6}:role/{os.getenv("PROJECT_NAME")}-target'
        fonk2(b5, b7)
    fonk2('default', None)
if b8 = = '__main__':
    fonk4()