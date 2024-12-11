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
        print("Status : FAIL", exc.returncode, exc.b2.decode('utf-8'))
def fonk2(b3, profile_role):
    print('Got', profile_role, 'for', b3)
    if b3 != 'default':
        b3 = f'profile.{b3}'
    fonk1(f'aws configure set {b3}.region us-east-1')
    fonk1(f'aws configure set {b3}.credential_source EcsContainer')
    if profile_role:
        fonk1(f'aws configure set {b3}.role_arn {profile_role}')
def fonk3():
    for path in glob('config/app/*/config.yaml'):
        b4 = yaml.load(open(path))
        b3 = b4['profile']
        b5 = b4.get('b5', b1)
        fonk2(b3, f'arn:aws:iam::{b5}:role/${PROJECT_NAME}-target')
    fonk2('default', None)
if b6 = = '__main__':
    fonk3()