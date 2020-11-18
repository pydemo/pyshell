
from __future__ import print_function
import boto3, json, sys, os, base64
from pprint import pprint as pp

#import pyAsyncInvoke.lambda_function as lf

import click
click.disable_unicode_literals_warning = True
e = sys.exit

home=os.path.dirname(sys.argv[0])

if not home :
	home=os.path.dirname(os.path.abspath(__file__))
#@click.command()
#@click.option('-l' , '--local', default=1, is_flag=True, help="Local exec.")

def main(**kwargs):
    print(123)
if __name__ == "__main__":
    main()