
import sys
def ensure_python3():
    if sys.version_info[0] != 3:
        print("This script requires Python 3")
        exit()
def run_construkt():
    from ConstruKT import ConstruKT
    config_path = '/media/pap/HDTOSHIBA1T/work/MIROR/TOOLS/python/constructions/cg_ak4/construkt/pap_pc_construkt.cfg'
    app = ConstruKT(config_path=config_path)
    app.run()
def main():
    ensure_python3()
    run_construkt()
if __name__ == "__main__":
    main()