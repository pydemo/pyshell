import json
import subprocess
from pprint import pprint as pp
def lambda_handler(evt, context):
    # TODO implement
    assert 'command' in evt
    
    cmd=[evt['command']]
    #pp(cmd)
    response = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    #pp(response)

    return {  
        'error': [],
        'stdout': response.decode('utf-8'),
        'stderr': ''
        
    }
