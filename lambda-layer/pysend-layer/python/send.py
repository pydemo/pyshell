import socket 
import sys
sys.path.append('/opt/python/lib/python3.7/site-packages')
import datetime as dt

from pprint import pprint
try:
	import cPickle as pickle
except:
	import pickle

e=sys.exit
import click
click.disable_unicode_literals_warning = True

n1=dt.datetime.now()

@click.command()
@click.option('-h', 	'--host',  default = socket.gethostname(), type=str, help = 'Host name.',   required=True )
@click.option('-p', 	'--port',  default = 12345, type=int, help = 'Port number.', required=True )

def main(**kwargs):

    s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0) 
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    host = kwargs['host'] 
    port = kwargs['port']
    s.connect((host, port))
    print ('Sending..'),
    with open('/tmp/test.csv') as fh:
        line=fh.readline()
        while line:
            pprint (line)
            pprint(pickle.dumps(line))
            s.send(line.encode())
            line=fh.readline()

    print ("Done Sending")
    s.shutdown(socket.SHUT_WR)
    s.close
    n2=dt.datetime.now()
    diff=(n2-n1)
    print (diff.seconds)
if __name__ == "__main__":
	main()