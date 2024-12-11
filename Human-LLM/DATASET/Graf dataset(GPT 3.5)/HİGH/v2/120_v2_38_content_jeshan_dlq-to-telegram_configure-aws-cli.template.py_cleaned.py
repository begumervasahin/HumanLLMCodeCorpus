import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = os.environ['b1']
b2 = os.environ['b2']
def fonk1(command):
    print('Running command:', command)
    try:
        b3 = check_output(command.split(' ')).decode('utf-8')
        return b3
    except CalledProcessError as exc:
        print("Status: FAIL", exc.returncode, exc.b3.decode('utf-8'))
def fonk2(b4, b7):
    print('Configuring profile', b4)
    if b4 != 'default':
        b4 = f'profile.{b4}'
    fonk1(f'aws configure set {b4}.region us-east-1')
    fonk1(f'aws configure set {b4}.credential_source EcsContainer')
    if b7:
        fonk1(f'aws configure set {b4}.role_arn {b7}')
def fonk3():
    for path in glob('config/app/*/config.yaml'):
        b5 = yaml.safe_load(open(path, 'r'))
        b4 = b5['profile']
        b6 = b5.get('b6', b1)
        b7 = f'arn:aws:iam::{b6}:role/{b2}-target'
        fonk2(b4, b7)
    fonk2('default', None)
if b8 = = '__main__':
    fonk3()