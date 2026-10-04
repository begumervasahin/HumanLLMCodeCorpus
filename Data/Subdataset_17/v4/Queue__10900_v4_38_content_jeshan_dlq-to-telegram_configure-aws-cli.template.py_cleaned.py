import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
ACCOUNT_ID = os.environ['ACCOUNT_ID']
def run(command):
    print('Running', command)
    try:
        output = check_output(command.split(' ')).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Status: FAIL", exc.returncode, exc.output.decode('utf-8'))
def configure_profile(profile_name, profile_role):
    print('Configuring', profile_name, 'with role', profile_role)
    if profile_name != 'default':
        profile_name = f'profile.{profile_name}'
    run(f'aws configure set {profile_name}.region us-east-1')
    run(f'aws configure set {profile_name}.credential_source EcsContainer')
    if profile_role:
        run(f'aws configure set {profile_name}.role_arn {profile_role}')
def main():
    for path in glob('config/app/*/config.yaml'):
        with open(path, 'r') as file:
            parsed = yaml.safe_load(file)
        profile_name = parsed['profile']
        account_id = parsed.get('account_id', ACCOUNT_ID)
        profile_role = f'arn:aws:iam::{account_id}:role/{os.environ["PROJECT_NAME"]}-target'
        configure_profile(profile_name, profile_role)
    configure_profile('default', None)
if __name__ == '__main__':
    main()