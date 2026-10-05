import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = 'us-east-1'
b2 = 'default'
b3 = 'config/app/*/config.yaml'
b4 = 'arn:aws:iam::{b8}:role/${PROJECT_NAME}-target'
def fonk1(command):
    print('Running command:', command)
    try:
        b5 = check_output(command.split()).decode('utf-8')
        return b5
    except CalledProcessError as exc:
        print("Command execution failed with return code:", exc.returncode)
        print("Error b5:", exc.b5.decode('utf-8'))
def fonk2(b6, role_arn):
    print('Configuring AWS profile:', b6)
    if b6 != b2:
        b6 = f'profile.{b6}'
    fonk1(f'aws configure set {b6}.region {b1}')
    fonk1(f'aws configure set {b6}.credential_source EcsContainer')
    if role_arn:
        fonk1(f'aws configure set {b6}.role_arn {role_arn}')
def fonk3():
    for path in glob(b3):
        b7 = yaml.load(open(path), Loader=yaml.FullLoader)
        b6 = b7['profile']
        b8 = b7.get('b8', os.environ['ACCOUNT_ID'])
        b9 = b4.format(b8=b8)
        fonk2(b6, b9)
    fonk2(b2, None)
if b10 = = '__main__':
    fonk3()