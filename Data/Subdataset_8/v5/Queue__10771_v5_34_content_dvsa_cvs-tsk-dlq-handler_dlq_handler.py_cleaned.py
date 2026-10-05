import json
import logging
import base64
import boto3
import datetime
import os
from pathlib import Path
from typing import List, Dict
from aws_xray_sdk.core import patch_all, xray_recorder
from boto3_type_annotations.lambda_ import Client as LambdaClient
patch_all()
logging.basicConfig(level=logging.INFO)
def get_source_queue_info(event_record: Dict[str, str]) -> Tuple[str, str]:
    sqs_arn = event_record.get('eventSourceARN')
    source_queue = sqs_arn.split(':')[5]
    source_environment = source_queue.rsplit('-', 1)[1]
    return source_queue, source_environment
def get_current_time() -> str:
    return datetime.datetime.utcnow().isoformat(timespec='minutes') + 'Z'
def prepare_payload(records: List[Dict]) -> Dict:
    source_queue, source_environment = get_source_queue_info(records[0])
    current_time = get_current_time()
    attachment = base64.b64encode(json.dumps(records, indent=2).encode('utf-8')).decode("utf-8")
    payload = {
        'message_type': 'email',
        'to': os.getenv('TO_EMAIL'),
        'template_id': os.getenv('TEMPLATE_ID'),
        'template_vars': {
            'source_queue': source_queue,
            'source_environment': source_environment
        },
        'attachment': attachment,
        'attachment_name': f'{source_queue}_dead_messages_{current_time}.json'
    }
    return payload
def invoke_notification_lambda(lambda_client: LambdaClient, payload: Dict) -> Dict:
    lambda_name = os.getenv('NOTIFY_LAMBDA_NAME')
    resp = lambda_client.invoke(FunctionName=lambda_name, Payload=json.dumps(payload))
    if resp.get('FunctionError') is not None:
        raise RuntimeError(f'{lambda_name} failed to notify with {payload}')
    else:
        return resp['Payload'].read()
@xray_recorder.capture('invoke')
def handler(event: Dict, context: Dict):
    lambda_client: LambdaClient = boto3.client('lambda')
    payload = prepare_payload(event.get('Records'))
    resp = invoke_notification_lambda(lambda_client, payload)
    return resp
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--event', help='Path to event json file', type=Path)
    args = parser.parse_args()
    with open(args.event) as event_file:
        evt = json.load(event_file)
    handler(evt, {})