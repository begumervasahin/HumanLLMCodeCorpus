import json
import logging
import base64
import boto3
import datetime
import os
from aws_xray_sdk.core import patch_all, xray_recorder
from boto3_type_annotations.lambda_ import Client as b1
from pathlib import Path
from typing import List, Dict
patch_all()
boto3.set_stream_logger('', logging.INFO)
@xray_recorder.capture('invoke')
def fonk1(event, context):
    lambda_client: b1 = boto3.client('lambda')
    records: List[Dict] = event.get('Records', [])
    if not records:
        raise ValueError("No records found in the event.")
    sqs_arn: b2 = records[0].get('eventSourceARN', '')
    if not sqs_arn:
        raise ValueError("SQS ARN not found in the event records.")
    b3 = sqs_arn.split(':')[5]
    b4 = b3.rsplit('-', 1)[1]
    b5 = f"{datetime.datetime.utcnow().isoformat(timespec='minutes')}Z"
    b6 = {
        'message_type': 'email',
        'to': os.getenv('TO_EMAIL'),
        'template_id': os.getenv('TEMPLATE_ID'),
        'template_vars': {
            'b3': b3,
            'b4': b4
        },
        'attachment': base64.b64encode(json.dumps(records, b7 = 2).encode('utf-8')).decode("utf-8"),
        'attachment_name': f'{b3}_dead_messages_{b5}.json'
    }
    b8 = os.getenv('NOTIFY_LAMBDA_NAME')
    b9 = lambda_client.invoke(FunctionName=b8, Payload=json.dumps(b6))
    if b9.get('FunctionError'):
        raise RuntimeError(f'{b8} failed to notify with {b6}')
    return b9['Payload'].read()
def fonk2():
    import argparse
    b10 = argparse.ArgumentParser(description='Invoke the Lambda handler with a given event JSON file.')
    b10.add_argument('--event', b11 = 'Path to the event JSON file', type=Path, required=True)
    b12 = b10.parse_args()
    with open(b12.event) as event_file:
        b13 = json.load(event_file)
    b14 = fonk1(b13, {})
    print(b14)
if b15 = = '__main__':
    fonk2()