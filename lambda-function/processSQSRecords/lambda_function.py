from __future__ import print_function
import json
from subprocess import Popen, PIPE, STDOUT

from pprint import pprint as pp  
def ncat(message):

    p = Popen(['/opt/nmap/4.14.181-108.257.amzn1.x86_64/bin/ncat 18.220.141.66 22000'], stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    stdout, stderr= p.communicate(input=message)
    #pp(response)
    p.wait() 
  
    return {  
        'error': {'code':p.returncode},
            #'{"code":'+json.dumps(p.returncode)+'}',
        'stdout': stdout.decode('utf-8'), 
        'stderr': stderr.decode('utf-8')
        
    }
    

def lambda_handler(event, context):
    for record in event['Records']:
       
       payload=record["body"]
       
       ret=ncat(b'PAYLOAD: %s\n' % payload.encode())
    return {'code':ret,'payload':payload}