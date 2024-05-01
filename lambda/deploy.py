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

    if event.get('queryStringParameters'):
        params = event['queryStringParameters']

        if params.get('name'):
            name = params['name']
            length = _calculate_length(name=name)
            res = f"Your name length is: {length}"
        else:
            logger.error("Cannot get key 'name'")

    else:
        logger.error("Cannot get parameters")

    body = {'res': res}
    
    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(body)
    }

    return response
