import os
from glob import glob
from subprocess import check_output, CalledProcessError
import yaml
DEFAULT_REGION = 'us-east-1'
DEFAULT_PROFILE_NAME = 'default'
AWS_CONFIG_PATH_PATTERN = 'config/app/*/config.yaml'
PROFILE_ROLE_FORMAT = 'arn:aws:iam::{account_id}:role/${PROJECT_NAME}-target'
def run_shell_command(command):
    print('Running command:', command)
    try:
        output = check_output(command.split()).decode('utf-8')
        return output
    except CalledProcessError as exc:
        print("Command execution failed with return code:", exc.returncode)
        print("Error output:", exc.output.decode('utf-8'))
def configure_aws_profile(profile_name, role_arn):
    print('Configuring AWS profile:', profile_name)
    if profile_name != DEFAULT_PROFILE_NAME:
        profile_name = f'profile.{profile_name}'
    run_shell_command(f'aws configure set {profile_name}.region {DEFAULT_REGION}')
    run_shell_command(f'aws configure set {profile_name}.credential_source EcsContainer')
    if role_arn:
        run_shell_command(f'aws configure set {profile_name}.role_arn {role_arn}')
def setup_aws_profiles():
    for path in glob(AWS_CONFIG_PATH_PATTERN):
        parsed_config = yaml.load(open(path), Loader=yaml.FullLoader)
        profile_name = parsed_config['profile']
        account_id = parsed_config.get('account_id', os.environ['ACCOUNT_ID'])
        profile_role = PROFILE_ROLE_FORMAT.format(account_id=account_id)
        configure_aws_profile(profile_name, profile_role)
    configure_aws_profile(DEFAULT_PROFILE_NAME, None)
if __name__ == '__main__':
    setup_aws_profiles()