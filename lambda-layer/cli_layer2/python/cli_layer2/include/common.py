
from os.path import join
FAILURE = 1 
LAYER_DIR = 'cli_layer'
PPL_DIR = join(LAYER_DIR, 'pipeline')
IN_DIR = 'in'
OUT_DIR = 'out'
TMPL=join(LAYER_DIR,'config','template','new_pipeline.txt')
EDITOR=r'C:\tmp\N\Notepad++\notepad++.exe'
TMP_DIR='/tmp'
def perr(err):
	print('#'*80)
	print('#'*80)
	print('ERROR:', err)
	print('#'*80)
	print('#'*80)