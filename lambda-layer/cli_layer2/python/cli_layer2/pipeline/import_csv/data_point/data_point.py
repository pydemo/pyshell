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



@timer (basename(__file__))
def main(**kwargs):
	"""
	DATA IMPORT
	For data import (line 963)
	4711	OCR20061	expiry not applicable	76000300	7600	TSH	Plasma	1	6240	MW	4.02726	9/21/2020 16:35	9/18/2020	Extra fields	mIU/L	
	API Name: MasQCDataTransfer_MW
	File NAme: Thermo_QC__test_20200921
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
			#pp(row)
			
			request={'LabId': row['LabLinkID'],  'Credentials': {'Login': "90096COM",
									  'Password': "ORTHO_ECONNECT"},
					'Points': {'MasQCDataTransferPoint_MW': 
								[{'AssayName' : row['Assay'],
								'BodyFluid' : row['Body Fluid'],
								'Concentration' : row['Concentration'],
								'InstrumentSerialNumber' : row['Serial Number'],
								'Level' : row['Level'],
								'MASControlLotExpirationDate' : datetime.now(),
								'MASControlLotNumber' : row['WCONTROLLOTNUMBER'],
								'ModelNumber' : row['model'],
								'ReagentExpirationDate' : datetime.now(),
								'ReagentNumber' : row['SubLot'],
								'RunDateTime' : datetime.now(),
								'SubLot' : row['SubLot'],
								'SubmissionDate' : datetime.now()
				}]} }
			#pp(request)
			if 1:
				responce=client.service.MasQCDataTransfer_MW(request=request)
				status=dict(Status= responce.Status,Errors= responce.Errors,ImportId= responce.ImportId)
			if status['Status'] not in ['OK']: log.debug(status)
			
			#e()
			if 1:
				
				preh='Status,Errors,ImportId'
				hdr=preh+','+','.join(reader.fieldnames)
				fmt=('{%s}' % hdr.replace(',','},{')).replace('{Conc. Conv. Unit}', row['Conc. Conv. Unit'])
				row.update(status)
				out=fmt.format(**row).strip().strip(',')
				if not done:
					done.append(hdr)
				done.append(out)
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
	python cli.py -nop 2 -r DEV -p import_csv\data_point \
		-pa in\import_csv\data_point\Thermo_QC__test_20200921_4471_1rec.csv out\import_csv\data_point\out.csv
		
	Number of input paramenters [-nop]:
		"2" - count of pipeline params in "-pa" option.
		
	Runtime environment [-r]:
		"DEV" - runtime name (DEV/UAT/PROD)
		
	Pipeline name [-p]:
		"import_csv\data_point" - pipeline used to import CSV file.
	
	Pipeline parameters [-pa]:
		"test.csv" 	 	- file to import
		"out_test.csv" 	- CSV import status log
		""")

		e(FAILURE)





