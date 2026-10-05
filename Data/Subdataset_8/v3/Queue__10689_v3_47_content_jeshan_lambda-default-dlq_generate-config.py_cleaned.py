import os
import sys
from os import mkdir, path
from mako.template import Template
AWS_REGIONS = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
CONFIG_DIR = 'config'
TEMPLATE_DIR = 'templates'
def create_directory(directory):
    try:
        mkdir(directory)
    except FileExistsError:
        pass
def save_template(template_path, data, output_dir=None):
    base_name = path.basename(template_path)
    output_path = template_path if not output_dir else path.join(output_dir, base_name)
    with open(output_path, 'w') as output_file:
        template = Template(filename=template_path)
        rendered_content = template.render(**data)
        output_file.write(rendered_content)
def generate_configuration(env):
    project_name = os.environ.get('PROJECT_NAME', 'lambda-default-dlq')
    public_bucket = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    private_bucket = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    save_template('configure-aws-cli.py', {'PROJECT_NAME': project_name})
    save_template('upload-private-config.sh', {'PROJECT_NAME': project_name, 'PRIVATE_BUCKET': private_bucket})
    save_template('upload-public-templates.sh',
                   {'PROJECT_NAME': project_name, 'PRIVATE_BUCKET': private_bucket, 'PUBLIC_BUCKET': public_bucket})
    save_template('deployment-pipeline.yaml', {'PROJECT_NAME': project_name}, output_dir=TEMPLATE_DIR)
    create_directory(CONFIG_DIR)
    create_directory(path.join(CONFIG_DIR, 'app', 'deployment'))
    create_directory(path.join(CONFIG_DIR, 'app', env))
    create_directory(path.join(CONFIG_DIR, 'app', 'deployment'))
    create_directory(path.join(CONFIG_DIR, 'app', env))
    general_config_path = path.join(CONFIG_DIR, 'config.yaml')
    if not path.exists(general_config_path):
        with open(general_config_path, 'w') as general_config:
            general_config.write(f)
    pipeline_config_path = path.join(CONFIG_DIR, 'app', 'deployment', 'pipeline.yaml')
    with open(pipeline_config_path, 'w') as pipeline_config:
        pipeline_config.write(f)
    base_config_path = path.join(CONFIG_DIR, 'app', env, 'base.yaml')
    with open(base_config_path, 'w') as base_config:
        base_config.write(f)
    for region in AWS_REGIONS:
        region_config_path = path.join(CONFIG_DIR, 'app', env, f'{region}.yaml')
        with open(region_config_path, 'w') as region_config:
            region_config.write(f)
if __name__ == '__main__':
    env_name = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    generate_configuration(env_name)