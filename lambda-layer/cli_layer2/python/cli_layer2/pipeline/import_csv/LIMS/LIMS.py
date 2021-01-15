import os, sys, csv, time, logging
import datetime, decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd
e=sys.exit

@timer (basename(__file__))
def main(**kwargs):
    pfmtd([kwargs], 'Kwargs.')
    params = kwargs['params']
    usage(params)

def check_pcount(params,pcount):
    if pcount == 1:
        assert type(params) in [str], params
        return
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
    
def usage(params):
    pcount=1
    try:
        check_pcount(params,pcount)
        assert pcount==1+1

    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p import_csv\LIMS -pa in_csv_file out_csv_file
        
    Number of input paramenters [-nop]:
        "1" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "import_csv\LIMS" - pipeline description.
    
    Pipeline parameters [-pa]:
        "in_csv_file" - param 0
        "out_csv_file" - param 1
""")])

        e(FAILURE)



    