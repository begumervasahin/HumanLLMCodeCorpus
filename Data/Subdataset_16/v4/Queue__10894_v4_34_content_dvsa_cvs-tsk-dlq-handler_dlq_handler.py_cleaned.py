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
    lamb: b1 = boto3.client('lambda')
    records: List[Dict] = event.get('Records')
    sqs_arn: b2 = records[0].get('eventSourceARN')
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
    b9 = lamb.invoke(FunctionName=b8, Payload=json.dumps(b6))
    if b9.get('FunctionError') is not None:
        raise RuntimeError(f'{b8} failed to notify with {b6}')
    else:
        return b9['Payload'].read()
if b10 = = '__main__':
    import argparse
    b11 = argparse.ArgumentParser(description='Invoke the Lambda function with a test event.')
    b11.add_argument('--event', b12 = 'Path to event JSON file', type=Path, required=True)
    b13 = b11.parse_args()
    with open(b13.event) as event_file:
        b14 = json.load(event_file)
    print(fonk1(b14, {}))