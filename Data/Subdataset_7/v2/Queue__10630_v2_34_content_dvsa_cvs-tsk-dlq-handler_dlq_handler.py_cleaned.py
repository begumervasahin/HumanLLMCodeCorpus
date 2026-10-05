import json
import logging
import base64
import datetime
import os
from typing import List, Dict
class class1:
    def fonk1(self, FunctionName, Payload):
        return {'FunctionError': None, 'Payload': b'Success'}
def fonk2(_, b1):
    logging.basicConfig(b1 = b1)
from aws_xray_sdk.core import patch_all, xray_recorder
patch_all()
fonk2('', logging.INFO)
@xray_recorder.capture('invoke')
def fonk3(event, context):
    b2 = class1()
    records: List[Dict] = event.get('Records')
    sqs_arn: b3 = records[0].get('eventSourceARN')
    b4 = sqs_arn.split(':')[5]
    b5 = b4.rsplit('-', 1)[1]
    b6 = f"{datetime.datetime.utcnow().isoformat(timespec='minutes')}Z"
    b7 = {
        'message_type': 'email',
        'to': os.getenv('TO_EMAIL'),
        'template_id': os.getenv('TEMPLATE_ID'),
        'template_vars': {
            'b4': b4,
            'b5': b5
        },
        'attachment': base64.b64encode(json.dumps(records, b8 = 2).encode('utf-8', errors='strict')).decode("utf-8", "strict"),
        'attachment_name': f'{b4}_dead_messages_{b6}.json'
    }
    b9 = os.getenv('NOTIFY_LAMBDA_NAME')
    b10 = b2.fonk1(FunctionName=b9, Payload=json.dumps(b7))
    if b10.get('FunctionError') is not None:
        raise RuntimeError(f'{b9} failed to notify with {b7}')
    else:
        return b10['Payload'].read()
if b11 = = '__main__':
    import argparse
    from pathlib import Path
    b12 = argparse.ArgumentParser()
    b12.add_argument('--event', b13 = 'Path to event json file', type=Path)
    b14 = b12.parse_args()
    with open(b14.event) as event_file:
        b15 = json.load(event_file)
    fonk3(b15, {})