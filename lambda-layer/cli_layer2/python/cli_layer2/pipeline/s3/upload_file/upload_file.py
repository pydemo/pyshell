import os, sys, csv, time, logging
import datetime, decimal
from os.path import split, join, isdir, basename, isfile
from pprint import pprint as pp
from include.utils import timer, get_err
from pathlib import Path
from include.common import *

from datetime import datetime

import boto3
from botocore.exceptions import NoCredentialsError
from botocore.config import Config
from boto3.session import Session


e=sys.exit
log = logging.getLogger('cli')


if 1:
	ACCESS_KEY=os.getenv('AWS_ACCESS_KEY_ID').strip("'")
	SECRET_KEY=os.getenv('AWS_SECRET_ACCESS_KEY').strip("'")
	SESSION_TOKEN=os.getenv('AWS_SESSION_TOKEN').strip("'")




@timer (basename(__file__))
def main(**kwargs):
	params = kwargs['params']
	usage(params)
	infn, bucket, outfn, region = params

	bs= Session(aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY, aws_session_token=SESSION_TOKEN, region_name=region)
	s3 = bs.resource('s3')
	client = bs.client('s3')

	uploaded=client.upload_file(infn, bucket, outfn)
	print("Upload Successful")

	pp(uploaded)

def usage(params):
	pcount=4
	try:
		assert len(params)==pcount, '%d - wrong parameter count (expecting %d)' % (len(params),pcount)
		infn, *_= params
		assert isfile(infn), 'Input file ""%s does not exists.' % infn
		assert os.getenv('AWS_ACCESS_KEY_ID'), 'you have to "SET AWS_ACCESS_KEY_ID=..."'
		assert os.getenv('AWS_SECRET_ACCESS_KEY'), 'you have to "SET AWS_SECRET_ACCESS_KEY=..."'
		assert os.getenv('AWS_SESSION_TOKEN'), 'you have to "SET AWS_SESSION_TOKEN=..."'
	except Exception as err:
		error=get_err()
		perr(error)
		print(r"""
USAGE:
	SET AWS_ACCESS_KEY_ID='***'
	SET AWS_SECRET_ACCESS_KEY='***'
	SET AWS_SESSION_TOKEN='***'

	..\oenv.bat & python  cli.py -nop 3 -r DEV -p s3\upload_file \
	-pa in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921.csv  ob-test-123 in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921.csv us-east-2
		
	Number of input paramenters [-nop]:
		"3" - count of pipeline params in "-pa" option.
		
	Runtime environment [-r]:
		"DEV" - runtime name (DEV/UAT/PROD)
		
	Pipeline name [-p]:
		"import_csv\upload_file" - pipeline used to upload CSV file to S3.
	
	Pipeline parameters [-pa]:
		"in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921_line_78.csv" 	- local file to upload
		"ob-test-123" 	- bucket name 
		"in\import_csv\reagent_version\Thermo_QC_MAS_VA_test_20200921_line_78.csv" 	- S3 file name
		"us-east-2" - upload region
""")

		e(FAILURE)





