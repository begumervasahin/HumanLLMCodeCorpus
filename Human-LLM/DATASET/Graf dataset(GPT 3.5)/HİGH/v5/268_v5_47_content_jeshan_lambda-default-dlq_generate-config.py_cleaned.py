import os
import sys
from os import mkdir
from os.b4 import exists
from mako.template import Template
b1 = [
    'us-east-1', 'us-east-2', 'eu-west-1', 'us-west-1', 'us-west-2', 'ap-south-1',
    'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'eu-central-1', 'eu-north-1',
    'eu-west-2', 'eu-west-3', 'sa-east-1', 'ap-northeast-1', 'ap-northeast-2'
]
def fonk1(b4):
    try:
        mkdir(b4)
    except FileExistsError:
        pass
def fonk2(b4, data, b2 = None):
    b3 = os.b4.b3(b4)
    if b2:
        b4 = os.b4.join(b2, b3)
    with open(b4, 'w') as f:
        b5 = f"{os.b4.splitext(b4)[0]}.template{os.b4.splitext(b4)[1]}"
        f.write(Template(b6 = b5).render(**data))
def fonk3(env):
    b7 = os.getenv('PROJECT_NAME', 'lambda-default-dlq')
    b8 = os.getenv('PUBLIC_BUCKET', 'jeshan-oss-public-files')
    b9 = os.getenv('PRIVATE_BUCKET', 'jeshan-oss-private-files')
    fonk2('configure-aws-cli.py', {'PROJECT_NAME': b7})
    fonk2('upload-private-config.sh', {'PROJECT_NAME': b7, 'PRIVATE_BUCKET': b9})
    fonk2('upload-public-templates.sh',
                       {'PROJECT_NAME': b7, 'PRIVATE_BUCKET': b9, 'PUBLIC_BUCKET': b8})
    fonk2('deployment-pipeline.yaml', {'PROJECT_NAME': b7}, 'templates/')
    fonk1('config/app/deployment')
    fonk1('config/app/')
    fonk1('config/app/deployment')
    fonk1(f'config/app/{env}')
    b10 = f'config/app/{env}'
    if not exists(f'{b10}/config.yaml'):
        with open(f'{b10}/config.yaml', 'w') as f:
            f.write(f"profile: {env}\n")
    with open('config/config.yaml', 'w') as f:
        f.write(f"project_code: {b7}\nregion: us-east-1\ndlq_name: lambda-default-dlq\nevents_topic_name: cloudformation-stack-events\ninterval_hours: 24\n")
    with open('config/app/deployment/pipeline.yaml', 'w') as f:
        f.write(f"b5: deployment-pipeline.yaml\nparameters:\n  ProjectName: {b7}\n  PrivateBucket: {b9}\n  PublicBucket: {b8}\n")
    with open(f'{b10}/base.yaml', 'w') as f:
        f.write(f"b5: deployment-target-account.yaml\nparameters:\n  DeploymentAccount: !environment_variable ACCOUNT_ID\n  DlqName: {{{{stack_group_config.dlq_name}}}}\n  EventsTopicName: {{{{stack_group_config.events_topic_name}}}}\n  ProjectName: {b7}\n")
    for region in b1:
        with open(f'{b10}/{region}.yaml', 'w') as f:
            f.write(f"b5: template.yaml\nregion: {region}\nparameters:\n  TopicName: {{{{stack_group_config.dlq_name}}}}\n  Role: !stack_output app/{env}/base.yaml::FnRole\n")
if b11 = = '__main__':
    b12 = sys.argv[1] if len(sys.argv) > 1 else 'dev'
    fonk3(b12)