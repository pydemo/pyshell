#!/usr/bin/python3
#
# Usage:
#   pylambdash [SHELLCOMMAND]
# 
from __future__ import print_function
import sys
import boto3, json, sys, os, base64
from pprint import pprint as pp
import pyAsyncInvoke.lambda_function as lf
from functools import partial
error = partial(print, file=sys.stderr)
#stdout = partial(print, file=sys.stdout)
import click
click.disable_unicode_literals_warning = True
e = sys.exit

home=os.path.dirname(sys.argv[0])

if not home :
	home=os.path.dirname(os.path.abspath(__file__))

SUCCESS=0
FAILURE=1

ex={True:'LOCAL|', False:'LAMBDA|'}

@click.command()
@click.option('-l' , '--local', default=False, is_flag=True, help="Local exec.")

def main(**kwargs):
    pp(kwargs)
    local=kwargs['local']
    if local:
        result = lf.lambda_handler(None, None)
    else:
        client = boto3.client('lambda', region_name='us-east-2')
        response = client.invoke(
            InvocationType='RequestResponse',
            #FunctionName=os.environ['LAMBDASH_FUNCTION'] or 'lambdash',
            FunctionName='pyAsyncInvoke',
            Payload='{"command":'+json.dumps(" ".join(sys.argv[1:]))+'}')
        result = json.load(response['Payload'])

    #pp(result)
    if 'errorMessage' in result: 
        print('#'*80)
        
        error(ex[local],result['errorMessage'])
        
        print('#'*80)
        
        exit(FAILURE)

    for line in result['stdout'].split('\n'):
        print(ex[local],line)

    if result['stderr']:
        print('#'*80)
        for line in result['stderr'].split('\n'):
            error(ex[local],line)
        print('#'*80)
        
    if result['error'] and 'code' in result['error'] and result['error']['code']:
        print(ex[local],'FAILURE (%s)' % result['error']['code'])
        
        exit(result['error']['code'])
    
    exit(SUCCESS)
if __name__ == "__main__":

    main()













