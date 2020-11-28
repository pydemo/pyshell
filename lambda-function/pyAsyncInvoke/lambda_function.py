import json
import asyncio
import time
import os, sys
from io import TextIOWrapper, BytesIO

SUCCESS=0

exit_code=SUCCESS
from functools import partial
error = partial(print, file=sys.stderr)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
async def sleep(delay, what):
    await asyncio.sleep(delay)
    print(what)
    eprint('ERROR:', what)

async def invoke(cmd, prefix=''):
    global exit_code
    import boto3, json, sys, os, base64
    from pprint import pprint as pp
    client = boto3.client('lambda', region_name='us-east-2')
    response = client.invoke(
        InvocationType='RequestResponse',
        FunctionName='pyshell',
        Payload='{"command":'+json.dumps(cmd)+'}')
    result = json.load(response['Payload'])
    
    
    if 'errorMessage' in result:
        eprint(result['errorMessage'])
        
        
    if result['stdout']:    
        for line in result['stdout'].strip().split('\n'):
            if line.strip():
                print('%s: ' % prefix, line)
    
    if result['stderr']:
        for line in result['stderr'].strip().split('\n'):
            if line.strip():
                eprint('ERROR: %s: ' % prefix, line)

        
    if result['error'] and 'code' in result['error'] and result['error']['code']:
        eprint('FAILURE (%s)' % result['error']['code'])
        exit_code=result['error']['code']
    
async def main ():
    
    load_1 = asyncio.create_task(invoke('python test.py', 'LOAD_1'))

    #load_2 = asyncio.create_task(invoke('ls -al /opt','LOAD_2'))
    
    #load_3 = asyncio.create_task(invoke('ls -al','LOAD_3'))
    
    print(f"started at {time.strftime('%X')}")
    
    await load_1
    #await load_2
    #await load_3

    print(f"finished at {time.strftime('%X')}")    
    

    
def lambda_handler(event, context):
    # TODO implement
    if 1:
        _stdout = sys.stdout
        _stderr = sys.stderr

        stdout=sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
        stderr=sys.stderr = TextIOWrapper(BytesIO(), sys.stderr.encoding)

    asyncio.run(main())
    
    if 1:
        sys.stdout = _stdout
        sys.stderr = _stderr
        stdout.seek(0)
        stderr.seek(0)
    return {
        'error': {'code':exit_code},
        'stdout': stdout.read(),
        'stderr': stderr.read()
    }