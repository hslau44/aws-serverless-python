import json
import logging
from package.utils import (
    calculate_length as _calculate_length,
    get_hello as _get_hello,
)

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': 'Hello, CDK! You have hit {}\n'.format(event['path'])
    }


def hello(event, context):
    # print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': _get_hello()
    }


def calculate(event, context):
    res = None
    if not event.get('name'):
        logger.error("Params does not have 'name'")
    
    name = event['name']
    length = _calculate_length(name=name)
    response = {'result': f'length of your name:  {length}'}
    return response
