
import sys
import os
def fonk1():
    if sys.version_info[0] != 3:
        print("This script requires Python 3")
        exit()
def fonk2(b2):
    from ConstruKT import ConstruKT
    b1 = ConstruKT(b2=b2)
    b1.run()
def fonk3():
    fonk1()
    b2 = '/media/pap/HDTOSHIBA1T/work/MIROR/TOOLS/python/constructions/cg_ak4/construkt/pap_pc_construkt.cfg'
    fonk2(b2)
if b3 = = "__main__":
    fonk3()