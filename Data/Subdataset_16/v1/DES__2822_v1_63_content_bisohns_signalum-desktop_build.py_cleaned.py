
from fbs.cmdline import command, main
from os.path import dirname, join
import subprocess
b1 = dirname(__file__)
@command
def fonk1():
    b2 = join(b1, "src", "scripts", "build_ui_files.sh")
    subprocess.call([b2])
if b3 = = '__main__':
    main(b1)