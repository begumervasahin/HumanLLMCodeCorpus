import os
import sys
from mako.template import Template
REGIONS = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
def create_directory(path):
    os.makedirs(path, exist_ok=True)
def save_template_file(path, data, directory=None):
    basename = os.path.basename(path)
    destination = os.path.join(directory, basename) if directory else path
    template_path = f"{os.path.splitext(path)[0]}.template{os.path.splitext(path)[1]}"
    with open(destination, 'w') as file:
        file.write(Template(filename=template_path).render(**data))
def generate_configuration(env):
    project_name = os.getenv('PROJECT_NAME', 'lambda-default-dlq')
    public_bucket = os.getenv('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    private_bucket = os.getenv('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    save_template_file('configure-aws-cli.py', {'PROJECT_NAME': project_name})
    save_template_file('upload-private-config.sh', {'PROJECT_NAME': project_name, 'PRIVATE_BUCKET': private_bucket})
    save_template_file('upload-public-templates.sh', {
        'PROJECT_NAME': project_name,
        'PRIVATE_BUCKET': private_bucket,
        'PUBLIC_BUCKET': public_bucket
    })
    save_template_file('deployment-pipeline.yaml', {'PROJECT_NAME': project_name}, 'templates/')
    create_directory('config')
    create_directory('config/app/')
    create_directory('config/app/deployment')
    create_directory(f'config/app/{env}')
    env_config_path = f'config/app/{env}/config.yaml'
    if not os.path.exists(env_config_path):
        with open(env_config_path, 'w') as file:
            file.write(f"profile: {env}\n")
    with open('config/config.yaml', 'w') as file:
        file.write(f)
    with open('config/app/deployment/pipeline.yaml', 'w') as file:
        file.write(f)
    with open(f'config/app/{env}/base.yaml', 'w') as file:
        file.write(f)
    for region in REGIONS:
        with open(f'config/app/{env}/{region}.yaml', 'w') as file:
            file.write(f)
if __name__ == '__main__':
    env_name = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    generate_configuration(env_name)