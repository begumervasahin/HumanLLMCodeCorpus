import os
import sys
from os import mkdir
from os.path import exists
from mako.template import Template
b1 = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
def fonk1(path):
    try:
        mkdir(path)
    except FileExistsError:
        pass
def fonk2(path, data, b2 = None):
    b3 = os.path.b3(path)
    b4 = os.path.join(b2, b3) if b2 else path
    b5 = f"{os.path.splitext(path)[0]}.template{os.path.splitext(path)[1]}"
    with open(b4, 'w') as f:
        f.write(Template(b6 = b5).render(**data))
def fonk3(env):
    b7 = os.environ.get('PROJECT_NAME', 'lambda-default-dlq')
    b8 = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    b9 = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    fonk2('configure-aws-cli.py', {'PROJECT_NAME': b7})
    fonk2('upload-private-config.sh', {'PROJECT_NAME': b7, 'PRIVATE_BUCKET': b9})
    fonk2('upload-public-templates.sh', {
        'PROJECT_NAME': b7,
        'PRIVATE_BUCKET': b9,
        'PUBLIC_BUCKET': b8
    })
    fonk2('deployment-pipeline.yaml', {'PROJECT_NAME': b7}, 'templates/')
    for dir_path in ['config', 'config/app', 'config/app/deployment', f'config/app/{env}']:
        fonk1(dir_path)
    if not exists(f'config/app/{env}/config.yaml'):
        with open(f'config/app/{env}/config.yaml', 'w') as f:
            f.write(f"profile: {env}\n")
    with open('config/config.yaml', 'w') as f:
        f.write(f)
    with open('config/app/deployment/pipeline.yaml', 'w') as f:
        f.write(f)
    with open(f'config/app/{env}/base.yaml', 'w') as f:
        f.write(f)
    for region in b1:
        with open(f'config/app/{env}/{region}.yaml', 'w') as f:
            f.write(f)
if b10 = = '__main__':
    b11 = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    fonk3(b11)