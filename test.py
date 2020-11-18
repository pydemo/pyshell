#!/usr/bin/python3
#
# Usage:
#   pylambdash [SHELLCOMMAND]
# 
from __future__ import print_function
import boto3, json, sys, os, base64
from pprint import pprint as pp

import pyAsyncInvoke.lambda_function as lf

import click
click.disable_unicode_literals_warning = True
e = sys.exit

home=os.path.dirname(sys.argv[0])

if not home :
	home=os.path.dirname(os.path.abspath(__file__))
@click.command()
@click.option('-l' , '--local', default=1, is_flag=True, help="Local exec.")

def main(**kwargs):
    pp(kwargs) 
    
    client = boto3.client('lambda', region_name='us-east-2')
    response = client.invoke(
        InvocationType='RequestResponse',
        #FunctionName=os.environ['LAMBDASH_FUNCTION'] or 'lambdash',
        FunctionName='pyAsyncInvoke',
        Payload='{"command":'+json.dumps(" ".join(sys.argv[1:]))+'}')
    result = json.load(response['Payload'])
    import pyAsyncInvoke.lambda_function as lf
    result = lf.lambda_handler(None, None)

    if 'errorMessage' in result:
        print('#'*80)
        os.write(sys.stderr.fileno(),b'\n')
        os.write(sys.stderr.fileno(), result['errorMessage'].encode('utf-8'))
        os.write(sys.stderr.fileno(),b'\n')
        print('#'*80)
        
        exit(1)
    for line in result['stdout'].split(r'\n'):
        os.write(sys.stdout.fileno(), line.encode('utf-8'))

    if result['stderr']:
        print('#'*80)
        for line in result['stderr'].split(r'\n'):
            os.write(sys.stderr.fileno(), line.encode('utf-8'))
        print('#'*80)
        
    if result['error'] and 'code' in result['error'] and result['error']['code']:
        print('FAILURE (%s)' % result['error']['code'])
        
        exit(result['error']['code'])
    exit(0)
if __name__ == "__main__":
    main()
