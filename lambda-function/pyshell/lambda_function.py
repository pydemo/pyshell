import json
import subprocess
from subprocess import Popen, PIPE

from pprint import pprint as pp
def lambda_handler(evt, context):
    # TODO implement
    assert 'command' in evt
    
    cmd=[evt['command']]
    #pp(cmd)
    p = subprocess.Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
    stdout, stderr = p.communicate()
    #pp(response)
    p.wait()
  
    return {  
        'error': {'code':p.returncode},
            #'{"code":'+json.dumps(p.returncode)+'}',
        'stdout': stdout.decode('utf-8'), 
        'stderr': stderr.decode('utf-8')
        
    }
