from os.path import join
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client
from zeep.transports import Transport
from zeep.cache import SqliteCache
from cli_layer.include.common import TMP_DIR

TLS_VERIFY = True

TLS_TIMEOUT=60

def get_client():
    session = Session()
    session.auth = HTTPBasicAuth('90138COM', 'ORTHO_ECONNECT')
    wsdl = 'http://www.maslablink.com/OrthoAPI/OrthoAPIService.asmx?WSDL'
    #wsdl = 'https://val.maslablink.com/OrthoAPI/OrthoAPIService.asmx?WSDL'
    
    if 1:
        fn=join(TMP_DIR,'sqlite.db')
        cache = SqliteCache(path=fn, timeout=TLS_TIMEOUT)
        transport=Transport(session=session, timeout=TLS_TIMEOUT, cache=cache)
        client = Client(wsdl, transport=transport)
    else:
        #inmemory
        client = Client(wsdl, transport=Transport(session=session, timeout=60, cache=SqliteCache()))
    
    client.transport.session.verify = TLS_VERIFY
    return client