
import os, sys, csv, time
from os.path import isfile, split, join, basename, isdir
import  importlib, subprocess
from collections import OrderedDict
from pprint import pprint as pp
from pathlib import Path

from cli_layer.include.common import *

import getpass
e=sys.exit

import traceback
try:
    import cStringIO
except ImportError:
    import io as cStringIO
    
def edit_file( fn):
    assert isfile(fn), fn
    if 1:
        subprocess.call([EDITOR, fn])
def get_err():
    err_log = cStringIO.StringIO()
    traceback.print_exc(file=err_log)
    return err_log.getvalue()
    
    
import logging
def init_logging(debug):
    bnf=basename(__file__)
    LOGGING_CONFIG = { 
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': { 
            'standard': { 
                '_format': '%(asctime)s|%(levelname)s|%(process)d|%(module)s.py|%(funcName)s|%(lineno)d| %(message)s',
                'format': '%(asctime)s|%(levelname)s|%(module)s.py|%(funcName)s|%(lineno)d| %(message)s',
                'datefmt':'%I:%M:%S'
            },
                'verbose': {
                    'format': 'ROOT: %(name)s: %(message)s'
                }
        },
        'handlers': { 
            'default': { 
                'level': 'DEBUG',
                'formatter': 'standard',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout',  # Default is stderr
            },
                'console': {
                    'level': 'DEBUG' if debug else 'INFO',
                    'class': 'logging.StreamHandler',
                    'formatter': 'verbose',
                },
        },
        'loggers': { 
            '': { 
                'handlers': ['console'],
                'level': 'DEBUG',
                'propagate': False
            },
            'cli': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            },
            'zeep': {
                    'level': 'DEBUG' if debug else 'INFO',
                    'propagate': True,
                    'handlers': ['console'],
                },
        } 
    }
    logging.config.dictConfig(LOGGING_CONFIG)

    

def timer(argument):
    def decorator(function):
        def wrapper(*args, **kwargs):
            start = time.time()
            
            result = function(*args, **kwargs)
            end = time.time()
            print("Elapsed %s:%s:---> [ %0.3f ] sec." % (argument, function.__name__, (end - start)))
            return result
        return wrapper
    return decorator


class dict2(dict):                                                              

    def __init__(self, **kwargs):                                               
        super(dict2, self).__init__(kwargs)                                     

    def __setattr__(self, key, value):                                          
        self[key] = value                                                       

    def __dir__(self):                                                          
        return self.keys()                                                      

    def __getattr__(self, key):                                                 
        try:                                                                    
            return self[key]                                                    
        except KeyError:                                                        
            raise AttributeError(key)                                           

    def __setstate__(self, state):                                              
        pass 


def import_module(file_path):
    print(file_path)
    bn=basename(file_path)
    mod_name,file_ext = os.path.splitext(os.path.split(file_path)[-1])
    spec = importlib.util.spec_from_file_location(mod_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if 1:
        sys.modules[mod_name] = module
    return module	
def get_module_loc(**kwargs):
    
    pipeline	= kwargs['pipeline']
    PPL_ROOT = kwargs['pipeline_root']
    assert(PPL_ROOT)
    _, ppl_name = split(pipeline)
    mod_fn = '%s.py' % ppl_name
    mod_dir = join(PPL_ROOT,PPL_DIR,pipeline)
    assert isdir(mod_dir), mod_dir
    mod_loc = join (mod_dir, mod_fn)
    assert isfile(mod_loc), mod_loc
    mod_file = Path(mod_loc).resolve()
    return mod_file

        
if __name__ == "__main__":
    if 1:
        conn = pyodbc.connect(connStr)
        cur=conn.cursor()
    trade_date= '2020-06-08'
    count(tname='ocean..EQ_EXEC_MASTER', trade_date="'%s'" % trade_date)
