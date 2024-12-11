import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
b1 = os.environ['b1']
b2 = os.environ['b2']
def fonk1(command):
    print('Running', command)
    try:
        b3 = check_output(command.split(' ')).decode('utf-8')
        return b3
    except CalledProcessError as exc:
        print("Status : FAIL", exc.returncode, exc.b3.decode('utf-8'))
def fonk2(b4, profile_role):
    print('Got', profile_role, 'for', b4)
    if b4 != 'default':
        b4 = f'profile.{b4}'
    fonk1(f'aws configure set {b4}.region us-east-1')
    fonk1(f'aws configure set {b4}.credential_source EcsContainer')
    if profile_role:
        fonk1(f'aws configure set {b4}.role_arn {profile_role}')
def fonk3():
    for path in glob('config/app/*/config.yaml'):
        b5 = yaml.load(open(path), Loader=yaml.FullLoader)
        b4 = b5['profile']
        b6 = b5.get('b6', b1)
        fonk2(b4, f'arn:aws:iam::{b6}:role/{b2}-target')
    fonk2('default', None)
if b7 = = '__main__':
    fonk3()