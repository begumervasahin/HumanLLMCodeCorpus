import json
import logging
import base64
import boto3
import datetime
import os
from pathlib import Path
from typing import List, Dict
from aws_xray_sdk.core import patch_all, xray_recorder
from boto3_type_annotations.lambda_ import Client as b11
patch_all()
logging.basicConfig(b1 = logging.INFO)
def fonk1(event_record: Dict[str, str]) -> Tuple[str, str]:
    b2 = event_record.get('eventSourceARN')
    b3 = b2.split(':')[5]
    b4 = b3.rsplit('-', 1)[1]
    return b3, b4
def fonk2() -> str:
    return datetime.datetime.utcnow().isoformat(b5 = 'minutes') + 'Z'
def fonk3(records: List[Dict]) -> Dict:
    b3, b4 = fonk1(records[0])
    b6 = fonk2()
    b7 = base64.b64encode(json.dumps(records, indent=2).encode('utf-8')).decode("utf-8")
    b8 = {
        'message_type': 'email',
        'to': os.getenv('TO_EMAIL'),
        'template_id': os.getenv('TEMPLATE_ID'),
        'template_vars': {
            'b3': b3,
            'b4': b4
        },
        'b7': b7,
        'attachment_name': f'{b3}_dead_messages_{b6}.json'
    }
    return b8
def fonk4(lambda_client: b11, b8: Dict) -> Dict:
    b9 = os.getenv('NOTIFY_LAMBDA_NAME')
    b10 = lambda_client.invoke(FunctionName=b9, Payload=json.dumps(b8))
    if b10.get('FunctionError') is not None:
        raise RuntimeError(f'{b9} failed to notify with {b8}')
    else:
        return b10['Payload'].read()
@xray_recorder.capture('invoke')
def fonk5(event: Dict, context: Dict):
    lambda_client: b11 = boto3.client('lambda')
    b8 = fonk3(event.get('Records'))
    b10 = fonk4(lambda_client, b8)
    return b10
if b12 = = '__main__':
    import argparse
    b13 = argparse.ArgumentParser()
    b13.add_argument('--event', b14 = 'Path to event json file', type=Path)
    b15 = b13.parse_args()
    with open(b15.event) as event_file:
        b16 = json.load(event_file)
    fonk5(b16, {})