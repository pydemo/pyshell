import socket  # Import socket module
import sys, time
from pprint import pprint
e=sys.exit
try:
    import cPickle as pickle
except:
    import pickle

try:
    import cStringIO
except ImportError:
    import io as cStringIO
    
    
def netcat_read_messages(**kargs):
    host, port = kargs['host'], kargs['port']
    #s = socket.socket()         # Create a socket object
    timed_out=True
    output = cStringIO.StringIO()
    while timed_out:
        try:
            #print 1
            s= socket.socket(socket.AF_INET, type=socket.SOCK_STREAM, proto=0)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            s.setblocking(False)
            s.settimeout(5)
            print (port)
            s.bind((host, port))        # Bind to the port
            
            s.listen(5)                 # Now wait for client connection.
            i=0
            while True:
                c, addr = s.accept()     # Establish connection with client.
                c.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                c.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                c.setblocking(False)
                c.settimeout(1)
                
                print ('Got connection from', addr)
                print ("Receiving...")
                
                i=0
                l = c.recv(1024)
                if 1:
                    for line in l.decode('utf-8').strip().split('\n'):
                        print(33,line)

                while (l):
                    l = c.recv(1024)
                    try:

                        for line in l.decode('utf-8').strip().split('\n'):
                            print(444,line)
                        
                    except:
                        pprint(l)
                        raise
                        
                    #print l
                    i +=1
                    if 0 and i>20:
                        f.close()
                        e(0)
                c.close()
                print ("Done Receiving")
            s.close()
        except socket.timeout as er1:
            err = er1.args[0]
            pprint(er1.args)
            print ('-----socket.timeout')
            timed_out=True
            
            s.close()
            
        except socket.error as er3:
            err = er3.args[0]
            print (er3.args )			
            
            s.close()
            timed_out=False
            raise er3
    

if __name__ == '__main__':
    netcat_read_messages(host=socket.gethostname(), port=12348)