import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = os.environ.get('b1')
b2 = os.environ.get('b2')
def fonk1(command):
    print(f'Running: {command}')
    try:
        b3 = check_output(command.split()).decode('utf-8')
        return b3
    except CalledProcessError as exc:
        print(f"Status: FAIL, Return Code: {exc.returncode}, Output: {exc.b3.decode('utf-8')}")
        return None
def fonk2(b6, b8):
    print(f'Configuring profile: {b6} with role: {b8}')
    b4 = f'profile.{b6}' if b6 != 'default' else b6
    fonk1(f'aws configure set {b4}.region us-east-1')
    fonk1(f'aws configure set {b4}.credential_source EcsContainer')
    if b8:
        fonk1(f'aws configure set {b4}.role_arn {b8}')
def fonk3():
    b5 = []
    for path in glob('config/app/*/config.yaml'):
        with open(path, 'r') as file:
            b5.append(yaml.safe_load(file))
    return b5
def fonk4():
    b5 = fonk3()
    for config in b5:
        b6 = config.get('profile')
        b7 = config.get('b7', b1)
        b8 = f'arn:aws:iam::{b7}:role/{b2}-target' if b6 else None
        fonk2(b6, b8)
    fonk2('default', None)
if b9 = = '__main__':
    fonk4()