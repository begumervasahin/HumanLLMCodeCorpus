import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
ACCOUNT_ID = os.environ.get('ACCOUNT_ID')
PROJECT_NAME = os.environ.get('PROJECT_NAME')
def run(command):
    print('Running:', command)
    try:
        output = check_output(command.split()).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Status: FAIL", exc.returncode, exc.output.decode('utf-8'))
        return None
def configure_profile(profile_name, profile_role):
    print('Got', profile_role, 'for', profile_name)
    aws_profile = f'profile.{profile_name}' if profile_name != 'default' else profile_name
    run(f'aws configure set {aws_profile}.region us-east-1')
    run(f'aws configure set {aws_profile}.credential_source EcsContainer')
    if profile_role:
        run(f'aws configure set {aws_profile}.role_arn {profile_role}')
def main():
    for path in glob('config/app/*/config.yaml'):
        with open(path, 'r') as file:
            parsed = yaml.safe_load(file)
        profile_name = parsed.get('profile')
        account_id = parsed.get('account_id', ACCOUNT_ID)
        profile_role = f'arn:aws:iam::{account_id}:role/{PROJECT_NAME}-target' if profile_name else None
        configure_profile(profile_name, profile_role)
    configure_profile('default', None)
if __name__ == '__main__':
    main()