import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
ACCOUNT_ID = os.environ.get('ACCOUNT_ID')
PROJECT_NAME = os.environ.get('PROJECT_NAME')
def run(command):
    print(f'Running: {command}')
    try:
        output = check_output(command.split()).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print(f"Status: FAIL, Return Code: {exc.returncode}, Output: {exc.output.decode('utf-8')}")
        return None
def configure_profile(profile_name, profile_role):
    print(f'Configuring profile: {profile_name} with role: {profile_role}')
    aws_profile = f'profile.{profile_name}' if profile_name != 'default' else profile_name
    run(f'aws configure set {aws_profile}.region us-east-1')
    run(f'aws configure set {aws_profile}.credential_source EcsContainer')
    if profile_role:
        run(f'aws configure set {aws_profile}.role_arn {profile_role}')
def load_configurations():
    configurations = []
    for path in glob('config/app/*/config.yaml'):
        with open(path, 'r') as file:
            configurations.append(yaml.safe_load(file))
    return configurations
def main():
    configurations = load_configurations()
    for config in configurations:
        profile_name = config.get('profile')
        account_id = config.get('account_id', ACCOUNT_ID)
        profile_role = f'arn:aws:iam::{account_id}:role/{PROJECT_NAME}-target' if profile_name else None
        configure_profile(profile_name, profile_role)
    configure_profile('default', None)
if __name__ == '__main__':
    main()