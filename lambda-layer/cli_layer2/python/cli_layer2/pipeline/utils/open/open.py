import os, sys, csv, time, logging
import datetime, decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err, edit_file
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd
e=sys.exit

@timer (basename(__file__))
def main(**kwargs):
    pfmtd([kwargs], 'Kwargs.')
    file = kwargs['params']
    usage(kwargs)
    pp(file)
    if file.startswith('cli'):
        edit_file('cli.py')
        return
    if file.startswith('utils'):
        edit_file(r'include\utils.py')
        return
    if file.startswith('common'):
        edit_file(r'include\common.py')
        return
    if file.startswith('template'):
        edit_file(r'config\template\new_pipeline.txt')
        return
    if file.startswith('readme'):
        edit_file(r'README.md')
        return                
    if 1: #ui
        if file.startswith('ui.utils'):
            edit_file(r'include\ui\utils.py')
            return
        if file.startswith('ui.common'):
            edit_file(r'include\ui\common.py')
            return
        
def check_pcount(params,pcount):
    if pcount == 1:
        assert type(params) in [str], params
        return
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
    
def usage(kwargs):
    pcount=1
    try:
        if kwargs['help']:
            assert False, 'Show usage.'
        params=kwargs['params']
        check_pcount(params,pcount)
        

    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p utils\open -pa file_to_open
        
    Number of input paramenters [-nop]:
        "1" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "utils\open" - pipeline description.
    
    Pipeline parameters [-pa]:
        "file_to_open" - param 0
""")])

        e(FAILURE)



    