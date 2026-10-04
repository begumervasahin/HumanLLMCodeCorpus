
import sys
def fonk1():
    if sys.version_info[0] != 3:
        print("This script requires Python 3")
        exit()
def fonk2():
    from ConstruKT import ConstruKT
    b1 = '/media/pap/HDTOSHIBA1T/work/MIROR/TOOLS/python/constructions/cg_ak4/construkt/pap_pc_construkt.cfg'
    b2 = ConstruKT(b1=b1)
    b2.run()
def fonk3():
    fonk1()
    fonk2()
if b3 = = "__main__":
    fonk3()