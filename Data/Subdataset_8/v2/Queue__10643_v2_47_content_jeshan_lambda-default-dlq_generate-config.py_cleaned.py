import os
import sys
from os import mkdir, path
from mako.template import Template
regions = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
def create_directory(directory):
    try:
        mkdir(directory)
    except FileExistsError:
        pass
def save_template_file(template_path, data, directory=None):
    basename = path.basename(template_path)
    output_path = template_path if not directory else f'{directory}/{basename}'
    with open(output_path, 'w') as output_file:
        template = Template(filename=template_path)
        rendered_content = template.render(**data)
        output_file.write(rendered_content)
def generate_configuration(env):
    project_name = os.environ.get('PROJECT_NAME', 'lambda-default-dlq')
    public_bucket = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    private_bucket = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    save_template_file('configure-aws-cli.py', {'PROJECT_NAME': project_name})
    save_template_file('upload-private-config.sh', {'PROJECT_NAME': project_name, 'PRIVATE_BUCKET': private_bucket})
    save_template_file('upload-public-templates.sh',
                       {'PROJECT_NAME': project_name, 'PRIVATE_BUCKET': private_bucket, 'PUBLIC_BUCKET': public_bucket})
    save_template_file('deployment-pipeline.yaml', {'PROJECT_NAME': project_name}, 'templates/')
    create_directory('config/app/deployment')
    create_directory('config')
    create_directory('config/app/')
    create_directory('config/app/deployment')
    create_directory(f'config/app/{env}')
    config_file_path = f'config/app/{env}/config.yaml'
    if not path.exists(config_file_path):
        with open(config_file_path, 'w') as config_file:
            config_file.write(f)
    with open('config/config.yaml', 'w') as general_config:
        general_config.write(f)
    with open('config/app/deployment/pipeline.yaml', 'w') as pipeline_config:
        pipeline_config.write(f)
    with open(f'config/app/{env}/base.yaml', 'w') as base_config:
        base_config.write(f)
    for region in regions:
        with open(f'config/app/{env}/{region}.yaml', 'w') as region_config:
            region_config.write(f)
if __name__ == '__main__':
    env_name = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    generate_configuration(env_name)