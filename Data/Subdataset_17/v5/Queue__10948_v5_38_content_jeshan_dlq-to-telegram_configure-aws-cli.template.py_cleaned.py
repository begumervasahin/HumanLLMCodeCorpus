import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
ACCOUNT_ID = os.getenv('ACCOUNT_ID')
def run_shell_command(command):
    print(f'Running: {command}')
    try:
        output = check_output(command.split()).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print(f"Status: FAIL. Return code: {exc.returncode}. Output: {exc.output.decode('utf-8')}")
        raise
def configure_aws_profile(profile_name, role_arn):
    print(f'Configuring profile: {profile_name} with role ARN: {role_arn}')
    profile_key_prefix = f'profile.{profile_name}' if profile_name != 'default' else profile_name
    run_shell_command(f'aws configure set {profile_key_prefix}.region us-east-1')
    run_shell_command(f'aws configure set {profile_key_prefix}.credential_source EcsContainer')
    if role_arn:
        run_shell_command(f'aws configure set {profile_key_prefix}.role_arn {role_arn}')
def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)
def main():
    for config_file_path in glob('config/app/*/config.yaml'):
        config = load_yaml_config(config_file_path)
        profile_name = config.get('profile')
        account_id = config.get('account_id', ACCOUNT_ID)
        role_arn = f'arn:aws:iam::{account_id}:role/{os.getenv("PROJECT_NAME")}-target'
        configure_aws_profile(profile_name, role_arn)
    configure_aws_profile('default', None)
if __name__ == '__main__':
    main()