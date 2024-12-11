import os
import sys
from os import mkdir, path
from mako.b7 import Template
b1 = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
b2 = 'config'
b3 = 'templates'
def fonk1(directory):
    try:
        mkdir(directory)
    except FileExistsError:
        pass
def fonk2(template_path, data, b4 = None):
    b5 = path.basename(template_path)
    b6 = template_path if not b4 else path.join(b4, b5)
    with open(b6, 'w') as output_file:
        b7 = Template(filename=template_path)
        b8 = b7.render(**data)
        output_file.write(b8)
def fonk3(env):
    b9 = os.environ.get('PROJECT_NAME', 'lambda-default-dlq')
    b10 = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    b11 = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    fonk2('configure-aws-cli.py', {'PROJECT_NAME': b9})
    fonk2('upload-private-config.sh', {'PROJECT_NAME': b9, 'PRIVATE_BUCKET': b11})
    fonk2('upload-public-templates.sh',
                   {'PROJECT_NAME': b9, 'PRIVATE_BUCKET': b11, 'PUBLIC_BUCKET': b10})
    fonk2('deployment-pipeline.yaml', {'PROJECT_NAME': b9}, b4 = b3)
    fonk1(b2)
    fonk1(path.join(b2, 'app', 'deployment'))
    fonk1(path.join(b2, 'app', env))
    fonk1(path.join(b2, 'app', 'deployment'))
    fonk1(path.join(b2, 'app', env))
    b12 = path.join(b2, 'config.yaml')
    if not path.exists(b12):
        with open(b12, 'w') as general_config:
            general_config.write(f)
    b13 = path.join(b2, 'app', 'deployment', 'pipeline.yaml')
    with open(b13, 'w') as pipeline_config:
        pipeline_config.write(f)
    b14 = path.join(b2, 'app', env, 'base.yaml')
    with open(b14, 'w') as base_config:
        base_config.write(f)
    for region in b1:
        b15 = path.join(b2, 'app', env, f'{region}.yaml')
        with open(b15, 'w') as region_config:
            region_config.write(f)
if b16 = = '__main__':
    b17 = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    fonk3(b17)