import json
import asyncio
import time
import os, sys
from io import TextIOWrapper, BytesIO

SUCCESS=0
_stdout = sys.stdout
_stderr = sys.stderr

stdout=sys.stdout = TextIOWrapper(BytesIO(), sys.stdout.encoding)
stderr=sys.stderr = TextIOWrapper(BytesIO(), sys.stderr.encoding)

exit_code=SUCCESS
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
async def say_after(delay, what):
    await asyncio.sleep(delay)
    #print(what)
    print(what)
    eprint('ERROR:', what)

async def invoke(cmd):
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
        
        
        
    for line in result['stdout'].split(r'\n'):
        print(line)
    
    if result['stderr']:
        eprint(result['stderr'])

        
    if result['error'] and 'code' in result['error'] and result['error']['code']:
        eprint('FAILURE (%s)' % result['error']['code'])
        
        exit_code=result['error']['code']
    
async def main ():
    task1 = asyncio.create_task(
        say_after(.5, 'hello'))

    task2 = asyncio.create_task(
        say_after(.5, 'world'))
    task3 = asyncio.create_task(invoke('ls -al'))
    
    print(f"started at {time.strftime('%X')}")
    
    await task1
    await task2
    await task3

    print(f"finished at {time.strftime('%X')}")    
    

    
def lambda_handler(event, context):
    # TODO implement

    asyncio.run(main())
    sys.stdout = _stdout
    sys.stderr = _stderr
    stdout.seek(0)
    stderr.seek(0)
    return {
        'error': {'code':exit_code},
        'stdout': stdout.read(),
        'stderr': stderr.read()
    }