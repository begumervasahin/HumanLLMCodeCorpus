'''
Created on 20181123
version 1.0
@author: korolev@limsi.fr, pap@limsi.fr
'''
import sys
import glob
import os
if sys.version_info[0] != 3:
    print("This script requires Python 3")
    exit()
from ConstruKT import ConstruKT
app = ConstruKT( config_path = '/media/pap/HDTOSHIBA1T/work/MIROR/TOOLS/python/constructions/cg_ak4/construkt/pap_pc_construkt.cfg' )
app.run()