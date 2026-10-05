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
def fonk3(records: List[Dict]) -> Tuple[b2, b2]:
    sqs_arn: b2 = records[0].get('eventSourceARN')
    b3 = sqs_arn.split(':')[5]
    b4 = b3.rsplit('-', 1)[1]
    return b3, b4
def fonk4(b3: b2) -> b2:
    b5 = datetime.datetime.utcnow().isoformat(timespec='minutes') + 'Z'
    return f'{b3}_dead_messages_{b5}.json'
def fonk5(records: List[Dict], b3: b2, b4: b2) -> Dict:
    b6 = {
        'message_type': 'email',
        'to': os.getenv('TO_EMAIL'),
        'template_id': os.getenv('TEMPLATE_ID'),
        'template_vars': {
            'b3': b3,
            'b4': b4
        },
        'attachment': base64.b64encode(json.dumps(records, b7 = 2).encode('utf-8', errors='strict')).decode("utf-8", "strict"),
        'attachment_name': fonk4(b3)
    }
    return b6
@xray_recorder.capture('invoke')
def fonk6(event, context):
    b8 = class1()
    records: List[Dict] = event.get('Records')
    b3, b4 = fonk3(records)
    b6 = fonk5(records, b3, b4)
    b9 = os.getenv('NOTIFY_LAMBDA_NAME')
    b10 = b8.fonk1(FunctionName=b9, Payload=json.dumps(b6))
    if b10.get('FunctionError') is not None:
        raise RuntimeError(f'{b9} failed to notify with {b6}')
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
    fonk6(b15, {})