#!/usr/bin/env python
#
# Usage:
#   pylambdash [SHELLCOMMAND]
# 
from __future__ import print_function
import boto3, json, sys, os, base64
from pprint import pprint as pp
client = boto3.client('lambda', region_name='us-east-2')
response = client.invoke(
    InvocationType='RequestResponse',
    #FunctionName=os.environ['LAMBDASH_FUNCTION'] or 'pylambdash',
    FunctionName='pylambdash',
    Payload='{"command":'+json.dumps(" ".join(sys.argv[1:]))+'}')
result = json.load(response['Payload'])
for line in result['stdout'].split(r'\n'):
    os.write(sys.stdout.fileno(), line.encode('utf-8'))

if result['stderr']:
    print('#'*80)
    for line in result['stderr'].split(r'\n'):
        os.write(sys.stderr.fileno(), line.encode('utf-8'))
    print('#'*80)
    
if result['error'] and 'code' in result['error']:
    print('FAILURE')
    exit(result['error']['code'])
exit(0)

