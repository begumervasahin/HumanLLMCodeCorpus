import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = os.environ['b1']
def fonk1(command):
    print('Running', command)
    try:
        b2 = check_output(command.split(' ')).decode('utf-8')
        return b2
    except CalledProcessError as exc:
        print("Status: FAIL", exc.returncode, exc.b2.decode('utf-8'))
def fonk2(b3, b6):
    print('Configuring', b3, 'with role', b6)
    if b3 != 'default':
        b3 = f'profile.{b3}'
    fonk1(f'aws configure set {b3}.region us-east-1')
    fonk1(f'aws configure set {b3}.credential_source EcsContainer')
    if b6:
        fonk1(f'aws configure set {b3}.role_arn {b6}')
def fonk3():
    for path in glob('config/app/*/config.yaml'):
        with open(path, 'r') as file:
            b4 = yaml.safe_load(file)
        b3 = b4['profile']
        b5 = b4.get('b5', b1)
        b6 = f'arn:aws:iam::{b5}:role/{os.environ["PROJECT_NAME"]}-target'
        fonk2(b3, b6)
    fonk2('default', None)
if b7 = = '__main__':
    fonk3()