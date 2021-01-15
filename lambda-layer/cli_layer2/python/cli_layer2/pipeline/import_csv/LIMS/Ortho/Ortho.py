import os, sys, csv, time, logging
import datetime as dt
from  datetime import datetime

from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd

import  cli_layer.include.wsdl as wsdl

e=sys.exit

log = logging.getLogger('cli')

SERVICE='VADataTransferOrthoPV_MTMS'


def get_params(**kwargs):
    params = kwargs['params']
    assert params, params
    cp=dict()
    if type(params) in [tuple]:
    
        cp = {pid:p for pid,p in enumerate(params)}
    else:
        assert type(params) in [str]
        cp[0]=params
    
    return cp, params
@timer (basename(__file__))
def main(**kwargs):
    """
    Reagent 
    Service Name: VADataTransferOrthoPV_MTMS
    File name: Ortho_LIMS_VA_API_export.csv
    """
    
    usage(**kwargs)
    cp, params=get_params(**kwargs)
    limit	= kwargs['lame_duck']
    infn, outfn = params
    client = wsdl.get_client()
    done=[]
    with open(infn, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for rid,row in enumerate(reader):
            #if rid==0: continue
            #pp(row)
            #e()
            request={'AssayName': row['ASSAY'],
                'BodyFluid': row['BODYFLUID'],
            'Credentials': {'Login': "90096COM",
                    'Password': "ORTHO_ECONNECT"},
            'GenExpirationDate': datetime.now(),
            'GenIntroductionDate': datetime.now(),
                'GenNumber': row['VA_NUMBER'],
                'GenVersion': row['VA_VERSION'],
                'Level': row['LEVEL'],
                'LowerLimitRange': row['LOWER_LIMIT'],
                #'MASControlLot':'%s/E' % row['CONTROLLOTNUMBER'],
                #'MASControlLotExpirationDate': datetime.now(),
                #'MASControlLotNumber': row['CONCCONVUNIT'],
                'Mean': row['MEAN_CONC'],
            'PVControlLot': '%s/E' % row['CONTROLLOTNUMBER'],
            'PVControlLotExpirationDate': datetime.now(),
            'PVControlLotNumber': 1,
                'ProductType': row['ASSAYTYPE'],
            #'ReagentExpirationDate': datetime.now(),
            #'ReagentIntroductionDate': datetime.now(),
            #'ReagentNumber': row['ReagentNumber'],
            #'ReagentVersion': row['ReagentVersion'],
            'RunDateTime': datetime.now(),
                'Sd':row['STDEV_CONC'],
                'SubLot': row['SUBLOT'],
            'UnitName': row['VENDER'],
                'UpperLimitRange': row['UPPER_LIMIT']
       }
            #pp(request)
            #pp(row)
            #e()
            if 1:
                service=client.service
                api  = getattr(service, SERVICE)
                #pp(api)
                #e()
                responce=api(request)
                #pp(dir(responce))
                
                if hasattr(responce,'ImportId'):
                    status=dict(Status= responce.Status,Errors= responce.Errors,ImportId=  hasattr(responce,'ImportId') if responce.ImportId else '')
                else:
                    status=dict(Status= responce.Status,Errors= responce.Errors)
            #log.debug(status)
            #pp(status)
            #e()
            pfmtd([status], 'status.')
            #e()
            if 1:
                err=dict(ErrorCode='',ErrorMessage='')
                if status['Status'] in ['ERROR']:
                    assert status['Errors']
                    serr= status['Errors']['Error'][0]
                    err['ErrorCode']=serr['ErrorCode']
                    err['ErrorMessage']=serr['ErrorMessage']

                    
                preh='Status,ErrorCode,ErrorMessage'
                hdr=preh+','+','.join(reader.fieldnames)
                fmt='{%s}' % hdr.replace(',','},{')
                row['Status']=status['Status']
                
                pfmtd([err], 'err.')
                row.update(err)
                out=fmt.format(**row).strip().strip(',')
                if not done:
                    done.append(hdr)
                done.append(out)
                #print(len(done))
            if limit and rid+1>=limit: 
                log.info('Lame duck break [%d]' % limit)
                break

    #e()
    if done:
        with open(outfn, 'w') as fh:
            fh.write('\n'.join(done))
        log.info('CSV log created at: %s' % outfn)
    else:
        log.warn('CSV log is empty.')
        
def check_pcount(params,pcount):
    
    if pcount == 1:
        assert params, 'Empty params.'
        assert type(params) in [str], params
        return
    
    assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
    
def usage(**kwargs):
    pfmtd([kwargs], 'Kwargs.')

    cp, params=get_params(**kwargs)
    pfmtd([cp], 'Params.')
    pcount=2
    try:
        if kwargs['help']:
            assert False, 'Show usage.'    
        check_pcount(params,pcount)
        
       
        
        infn, outfn = params
        assert isfile(infn), 'Input file "%s" does not exists.' % infn
        if isfile(outfn): os.remove(outfn); assert not isfile(outfn), 'Cannot delete existing output file "%s".' % outfn

        out_dir, outbn = split(outfn)
        if out_dir and not isdir(out_dir):
            os.makedirs(out_dir)
            assert isdir(out_dir), 'Cannot create output dir "%s"' % out_dir

    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p import_csv\LIMS\Ortho -pa in_csv_file out_csv_file
        
    Number of input paramenters [-nop]:
        "2" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "import_csv\LIMS\Ortho" - pipeline description.
    
    Pipeline parameters [-pa]:
        "in_csv_file" - param 0
        "out_csv_file" - param 1
""")])

        e(FAILURE)



    