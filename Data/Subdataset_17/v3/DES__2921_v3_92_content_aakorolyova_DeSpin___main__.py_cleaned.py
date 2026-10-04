
import sys
import os
def ensure_python3():
    if sys.version_info[0] != 3:
        print("This script requires Python 3")
        exit()
def initialize_and_run_construkt(config_path):
    from ConstruKT import ConstruKT
    app = ConstruKT(config_path=config_path)
    app.run()
def main():
    ensure_python3()
    config_path = '/media/pap/HDTOSHIBA1T/work/MIROR/TOOLS/python/constructions/cg_ak4/construkt/pap_pc_construkt.cfg'
    initialize_and_run_construkt(config_path)
if __name__ == "__main__":
    main()