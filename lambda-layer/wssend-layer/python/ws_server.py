import sys
sys.path.append('/opt/python/lib/python3.7/site-packages')

import os
import asyncio
import websockets
from ec2_metadata import ec2_metadata

from functools import wraps

import click
click.disable_unicode_literals_warning = True

def coro(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        return asyncio.run(f(*args, **kwargs))

    return wrapper
    

class Server:
    def __init__(self, host, port):
        self.host=host
        self.port=str(port)
    def get_port(self):
        return os.getenv('WS_PORT', self.port)

    def get_host(self):
        print(self.host)
        return os.getenv('WS_HOST', self.host)


    def start(self):
        return websockets.serve(self.handler, self.get_host(), self.get_port())

    async def handler(self, websocket, path):
      async for message in websocket:
        print('server received :', message)
        await websocket.send(message)

@click.command()
@coro
@click.option('-h', 	'--host', default=ec2_metadata.public_hostname, type=str, help = 'Host name.',   required=True )
@click.option('-p', 	'--port', default = 22000, type=int, help = 'Port number.', required=True )        
def main(**kwargs):
    host = kwargs['host'] 
    port = kwargs['port']
    ws = Server(host=host, port=port)
    asyncio.get_event_loop().run_until_complete(ws.start())
    asyncio.get_event_loop().run_forever()
  
if __name__ == '__main__':
    main()