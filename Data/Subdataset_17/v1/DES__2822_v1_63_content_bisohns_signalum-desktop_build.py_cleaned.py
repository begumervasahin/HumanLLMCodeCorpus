
from fbs.cmdline import command, main
from os.path import dirname, join
import subprocess
project_dir = dirname(__file__)
@command
def ui_files():
    script_path = join(project_dir, "src", "scripts", "build_ui_files.sh")
    subprocess.call([script_path])
if __name__ == '__main__':
    main(project_dir)