import os, sys, csv, time, logging
import datetime as dt
from  datetime import datetime
import  decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer, get_err
from pathlib import Path
from cli_layer.include.common import *
from cli_layer.include.fmt import  pfmt, psql, pfmtd


import  cli_layer.include.wsdl as wsdl


e=sys.exit


log = logging.getLogger('cli')

SERVICE='VADataTransferMasQC_MTMS'


def get_params(**kwargs):
    params = kwargs['params']
    pp(kwargs)
    assert params, params
    cp=dict()
    if type(params) in [tuple]:
    
        cp = {pid:p for pid,p in enumerate(params)}
    else:
        assert type(params) in [str]
        cp[0]=params
    pfmtd([cp], 'Params.')
    return cp, params
    
"""
 'input': {'VADataTransferMasQC_MTMS': {'vaDataTransferMasQCMTMSrequest': 
 {'AssayName': <class 'str'>,
       'BodyFluid': <class 'str'>,
       'Credentials': {'Login': <class 'str'>,
                       'Password': <class 'str'>},
       'GenExpirationDate': <class 'datetime.datetime'>,
       'GenIntroductionDate': <class 'datetime.datetime'>,
       'GenNumber': <class 'str'>,
       'GenVersion': <class 'str'>,
       'Level': <class 'str'>,
       'LowerLimitRange': <class 'decimal.Decimal'>,
       'MASControlLot': <class 'str'>,
       'MASControlLotExpirationDate': <class 'datetime.datetime'>,
       'MASControlLotNumber': <class 'str'>,
       'Mean': <class 'decimal.Decimal'>,
       'PVControlLot': <class 'str'>,
       'PVControlLotExpirationDate': <class 'datetime.datetime'>,
       'PVControlLotNumber': <class 'str'>,
       'ProductType': <class 'str'>,
       'ReagentExpirationDate': <class 'datetime.datetime'>,
       'ReagentIntroductionDate': <class 'datetime.datetime'>,
       'ReagentNumber': <class 'str'>,
       'ReagentVersion': <class 'str'>,
       'RunDateTime': <class 'datetime.datetime'>,
       'Sd': <class 'decimal.Decimal'>,
       'SubLot': <class 'str'>,
       'UnitName': <class 'str'>,
       'UpperLimitRange': <class 'decimal.Decimal'>}}},
"""
 
@timer (basename(__file__))
def main(**kwargs):
    """
    Reagent 
    Service Name: VADataTransferMasQC_MTMS
    File name: MAS_LIMS_VA_API_export
    """
    usage(**kwargs)
    cp, params=get_params(**kwargs)
    limit	= kwargs['lame_duck']
    infn_, outfn_ = params
    PPL_ROOT = kwargs['pipeline_root']
    infn=join(PPL_ROOT,LAYER_DIR, infn_)
    outfn=join(TMP_DIR,outfn_)
    client = wsdl.get_client()
    done=[]
    print('*START*'*5)
    print(infn)
    #e()
    import unicodecsv as csv
    with open(infn, mode="rb") as csvfile:
        reader = csv.DictReader(csvfile)

        for rid,row in enumerate(reader):
            #pp(row)
            #e()
            request={'AssayName': row['ASSAY'],
                'BodyFluid': row['BODYFLUID'],
            'Credentials': {'Login': "90138COM",
                    'Password': "ORTHO_ECONNECT"},
            'GenExpirationDate': datetime.now(),
            'GenIntroductionDate': datetime.now(),
                'GenNumber': row['VA_NUMBER'],
                'GenVersion': row['VA_VERSION'],
                'Level': row['LEVEL'],
                'LowerLimitRange': row['LOWER_LIMIT'],
                'MASControlLot':'%s' % row['CONTROLLOTNUMBER'],
                'MASControlLotExpirationDate': datetime.now(),
                'MASControlLotNumber': 1,
                'Mean': row['MEAN_CONC'],
            #'PVControlLot': 1,
            #'PVControlLotExpirationDate': datetime.now(),
            #'PVControlLotNumber': 1,
                'ProductType': row['ASSAYTYPE'],
            #'ReagentExpirationDate': datetime.now(),
            #'ReagentIntroductionDate': datetime.now(),
            #'ReagentNumber': row['ReagentNumber'],
            #'ReagentVersion': row['ReagentVersion'],
            'RunDateTime': datetime.now(),
                'Sd':row['STDEV_CONC'],
                'SubLot': row['SUBLOT'],
            #'UnitName': row['VENDER'],
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
            #if status['Status'] not in ['OK']: log.debug(status)
            pfmtd([status], 'status.')
            #e()
            #time.sleep(1)
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
                #pp(err)
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

    params = kwargs['params']
    PPL_ROOT = kwargs['pipeline_root']
    pcount=2
    try:
        if kwargs['help']:
            assert False, 'Show usage.'    
        check_pcount(params,pcount)
        
       
        
        infn_, outfn = params
        infn  = join(PPL_ROOT,LAYER_DIR, infn_)
        assert isfile(infn), 'Input file "%s" does not exists.' % infn
        if isfile(outfn): os.remove(outfn); assert not isfile(outfn), 'Cannot delete existing output file "%s".' % outfn

        _out_dir, outbn = split(outfn)
        out_dir= join(TMP_DIR,_out_dir)
        print(12345,out_dir)
        if out_dir and not isdir(out_dir):
            os.makedirs(out_dir)
            assert isdir(out_dir), 'Cannot create output dir "%s"' % out_dir
        
        

    except Exception as err:
        error=get_err()
        perr(error)
        pfmtd([dict(Usage=r"""
USAGE:

    python cli.py -nop 1 -r DEV -p import_csv\LIMS\MAS -pa in_csv_file out_csv_file
        
    Number of input paramenters [-nop]:
        "2" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "import_csv\LIMS\MAS" - pipeline description.
    
    Pipeline parameters [-pa]:
        "in_csv_file" - param 0
        "out_csv_file" - param 1
""")])

        e(FAILURE)



    