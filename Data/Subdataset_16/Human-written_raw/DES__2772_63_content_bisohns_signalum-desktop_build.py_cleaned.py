
from fbs.cmdline import command
from os.path import dirname
import subprocess
import fbs.cmdline
b1 = dirname(__file__)
@command
def fonk1():
    subprocess.call([b1 + "src/scripts/build_ui_files.sh"])
if b2 = = '__main__':
    fbs.cmdline.main(b1)