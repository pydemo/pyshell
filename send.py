import socket 
import sys
import datetime as dt

from pprint import pprint
try:
	import cPickle as pickle
except:
	import pickle

e=sys.exit
n1=dt.datetime.now()
#s = socket.socket()
s = socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0) 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_CORK, 1)

host = socket.gethostname() 
port = 12348           # Reserve a port for your service.
s.connect((host, port))
#f = open('/dump2/oats/101316/rawdata/pr1lsmars11.20161013.TransOrd.dat.gz') 
#f = open('/dump2/oats/101316/rawdata/MatchIt_20161013.dat.gz','rb')
#f = open('/Bic/scripts/oats/py27/bin/file.txt','rb')
print ('Sending..'),
#l = f.read(100*1024)
with open('test.csv') as fh:
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
e(0)