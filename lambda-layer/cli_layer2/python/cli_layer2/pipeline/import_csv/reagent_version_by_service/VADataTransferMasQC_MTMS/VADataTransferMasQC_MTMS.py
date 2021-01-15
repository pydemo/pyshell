import os, sys, csv, time, logging
import datetime, decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from cli_layer.include.utils import timer
from pathlib import Path
from cli_layer.include.common import *


from datetime import datetime

import  cli_layer.include.wsdl as wsdl


e=sys.exit


log = logging.getLogger('cli')

SERVICE='VADataTransferMasQC_MTMS'

#@timer (basename(__file__))
def main(**kwargs):
    """
    Reagent 
    Service Name: VADataTransferMasQC_MTMS
    File name: Thermo_VA_Ominicore_example
    """
 
    params = kwargs['params']
    usage(params)
    limit	= kwargs['lame_duck']
    infn, outfn = params

    

    client = wsdl.get_client()

    done=[]
    with open(infn, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for rid,row in enumerate(reader):
            pp(row)
            
            request={'AssayName': row['Assay'],
            'BodyFluid': row['Body Fluid'],
            'Credentials': {'Login': "90096COM",
                    'Password': "ORTHO_ECONNECT"},
            'GenExpirationDate': datetime.now(),
            'GenIntroductionDate': datetime.now(),
            'GenNumber': row['VA_Number'],
            'GenVersion': row['VA_Version'],
            'Level': row['Level'],
            'LowerLimitRange': row['Lower_Limit'],
            'MASControlLot':'%s/E' % row['WCONTROLLOTNUMBER'],
            'MASControlLotExpirationDate': datetime.now(),
            'MASControlLotNumber': row['WCONTROLLOTNUMBER'],
            'Mean': row['Mean_Conc'],
            'PVControlLot': 1,
            'PVControlLotExpirationDate': datetime.now(),
            'PVControlLotNumber': 1,
            'ProductType': row['Assay Type'],
            'ReagentExpirationDate': datetime.now(),
            'ReagentIntroductionDate': datetime.now(),
            'ReagentNumber': row['VA_Number'],
            'ReagentVersion': row['VA_Version'],
            'RunDateTime': datetime.now(),
            'Sd':0,
            'SubLot': row['SubLot'],
            'UnitName': row['Assay'],
       'UpperLimitRange': row['Upper_Limit']
       }
            pp(request)
            pp(row)
            #e()
            if 1:
                service=client.service
                api  = getattr(service, SERVICE)
                pp(api)
                #e()
                responce=api(request)
                pp(dir(responce))
                if hasattr(responce,'ImportId'):
                    status=dict(Status= responce.Status,Errors= responce.Errors,ImportId=  hasattr(responce,'ImportId') if responce.ImportId else '')
                else:
                    status=dict(Status= responce.Status,Errors= responce.Errors)
            if status['Status'] not in ['OK']: log.debug(status)
            
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
                fmt=('{%s}' % hdr.replace(',','},{')).replace('{Conc. Conv. Unit}', row['Conc. Conv. Unit'])
                row['Status']=status['Status']
                #pp(err)
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
        
def usage(params):
    pcount=2
    try:
        assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
        infn, outfn = params
        assert isfile(infn), 'Input file ""%s does not exists.' % infn
        if isfile(outfn): os.remove(outfn); assert not isfile(outfn), 'Cannot delete existing output file "%s".' % outfn

        out_dir, outbn = split(outfn)
        if out_dir and not isdir(out_dir):
            os.makedirs(out_dir)
            assert isdir(out_dir), 'Cannot create output dir "%s"' % out_dir
    except Exception as err:
        perr(err)
        print("""
USAGE:
    python cli.py -nop 2 -r DEV -p import_csv\reagent_version \
        -pa in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921_line_78.csv out\import_csv\reagent_version\out.csv
        
    Number of input paramenters [-nop]:
        "2" - count of pipeline params in "-pa" option.
        
    Runtime environment [-r]:
        "DEV" - runtime name (DEV/UAT/PROD)
        
    Pipeline name [-p]:
        "import_csv\reagent_version" - pipeline used to import CSV file.
    
    Pipeline parameters [-pa]:
        "in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921_line_78.csv" 	 	- file to import
        "out\import_csv\reagent_version\out.csv" 	- CSV import status log
        """)

        e(FAILURE)





