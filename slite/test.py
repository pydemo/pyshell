from __future__ import print_function
#https://rogerbinns.github.io/apsw/example.html
# some python 2 and 3 comnpatibility tweaks
import sys
py3=sys.version_info >= (3, 0)
def inext(v):  # next value from iterator
    return next(v) if py3 else v.next()

import os
import time
import apsw

###
### Check we have the expected version of apsw and sqlite
###

print ("      Using APSW file",apsw.__file__)                # from the extension module
print ("         APSW version",apsw.apswversion())           # from the extension module
print ("   SQLite lib version",apsw.sqlitelibversion())      # from the sqlite library code
print ("SQLite header version",apsw.SQLITE_VERSION_NUMBER)   # from the sqlite header file at compile time
