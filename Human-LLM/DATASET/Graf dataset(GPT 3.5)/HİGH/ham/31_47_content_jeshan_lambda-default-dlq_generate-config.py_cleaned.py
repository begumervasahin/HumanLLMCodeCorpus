import os
import sys
from os import mkdir
from os.path import exists
from mako.template import Template
b1 = 'us-east-1,us-east-2,eu-west-1,us-west-1,us-west-2,ap-south-1,ap-southeast-1,ap-southeast-2,ca-central-1,eu-central-1,eu-north-1,eu-west-2,eu-west-3,sa-east-1,ap-northeast-1,ap-northeast-2'.split(
    ',')
def fonk1(path):
    try:
        mkdir(path)
    except:
        pass
def fonk2(path, data, b2 = None):
    b3 = path[(path.rindex('/') + 1) if '/' in path else 0:]
    with open(path if not b2 else f'{b2}/{b3}', 'w') as f:
        b4 = path[:path.rindex('.') + 1] + 'template.' + path[path.rindex('.') + 1:]
        f.write(Template(b5 = b4).render(**data))
def fonk3(env):
    b6 = os.environ.get('PROJECT_NAME', 'lambda-default-dlq')
    b7 = os.environ.get('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    b8 = os.environ.get('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    fonk2('configure-aws-cli.py', {'PROJECT_NAME': b6})
    fonk2('upload-private-config.sh', {'PROJECT_NAME': b6, 'PRIVATE_BUCKET': b8})
    fonk2('upload-public-templates.sh',
                       {'PROJECT_NAME': b6, 'PRIVATE_BUCKET': b8, 'PUBLIC_BUCKET': b7})
    fonk2('deployment-pipeline.yaml', {'PROJECT_NAME': b6}, 'templates/')
    fonk1('config/app/deployment')
    fonk2('pipeline.yaml', {'PUBLIC_BUCKET': b7, 'PRIVATE_BUCKET': b8},
                       'config/app/deployment/')
    fonk1('config')
    fonk1('config/app/')
    fonk1('config/app/deployment')
    fonk1(f'config/app/{env}')
    if not exists(f'config/app/{env}/config.yaml'):
        with open(f'config/app/{env}/config.yaml', 'w') as f:
            f.write(f)
    with open('config/config.yaml', 'w') as f:
        f.write(f)
    with open('config/app/deployment/pipeline.yaml', 'w') as f:
        f.write(f)
    with open(f'config/app/{env}/base.yaml', 'w') as f:
        f.write(f)
    for region in b1:
        with open(f'config/app/{env}/{region}.yaml', 'w') as f:
            f.write(f)
if b9 = = '__main__':
    b10 = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    fonk3(b10)