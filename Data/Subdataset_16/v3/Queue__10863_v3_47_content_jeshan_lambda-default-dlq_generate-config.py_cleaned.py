import os
import sys
from mako.template import Template
b1 = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2',
    'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1',
    'eu-central-1', 'eu-north-1', 'eu-west-2', 'eu-west-3', 'sa-east-1',
    'ap-northeast-1', 'ap-northeast-2'
]
def fonk1(path):
    os.makedirs(path, b2 = True)
def fonk2(path, data, b3 = None):
    b4 = os.path.b4(path)
    b5 = os.path.join(b3, b4) if b3 else path
    b6 = f"{os.path.splitext(path)[0]}.template{os.path.splitext(path)[1]}"
    with open(b5, 'w') as file:
        file.write(Template(b7 = b6).render(**data))
def fonk3(env):
    b8 = os.getenv('PROJECT_NAME', 'lambda-default-dlq')
    b9 = os.getenv('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    b10 = os.getenv('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    fonk2('configure-aws-cli.py', {'PROJECT_NAME': b8})
    fonk2('upload-private-config.sh', {'PROJECT_NAME': b8, 'PRIVATE_BUCKET': b10})
    fonk2('upload-public-templates.sh', {
        'PROJECT_NAME': b8,
        'PRIVATE_BUCKET': b10,
        'PUBLIC_BUCKET': b9
    })
    fonk2('deployment-pipeline.yaml', {'PROJECT_NAME': b8}, 'templates/')
    fonk1('config')
    fonk1('config/app/')
    fonk1('config/app/deployment')
    fonk1(f'config/app/{env}')
    b11 = f'config/app/{env}/config.yaml'
    if not os.path.exists(b11):
        with open(b11, 'w') as file:
            file.write(f"profile: {env}\n")
    with open('config/config.yaml', 'w') as file:
        file.write(f)
    with open('config/app/deployment/pipeline.yaml', 'w') as file:
        file.write(f)
    with open(f'config/app/{env}/base.yaml', 'w') as file:
        file.write(f)
    for region in b1:
        with open(f'config/app/{env}/{region}.yaml', 'w') as file:
            file.write(f)
if b12 = = '__main__':
    b13 = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    fonk3(b13)