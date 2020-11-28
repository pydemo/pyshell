import json
import sys
sys.path.insert(0, '/opt')
import test_module as tm


def lambda_handler(event, context):
    # TODO implement
    tm.print_hello_world()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
