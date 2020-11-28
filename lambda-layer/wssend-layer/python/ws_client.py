import sys
sys.path.append('/opt/python/lib/python3.7/site-packages')
import socket
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


@click.command()
@coro
@click.option('-h', 	'--host',  type=str, help = 'Host name.',   required=True )
@click.option('-p', 	'--port',  default = 22000, type=int, help = 'Port number.', required=True )
async def msg(**kwargs):
    host = kwargs['host'] 
    port = kwargs['port']
    async with websockets.connect('ws://%s:%s' % (host, port)) as websocket:

        await websocket.send('test message')
        msg = await websocket.recv()
        print(msg)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(msg())
    #asyncio.get_event_loop().run_forever()