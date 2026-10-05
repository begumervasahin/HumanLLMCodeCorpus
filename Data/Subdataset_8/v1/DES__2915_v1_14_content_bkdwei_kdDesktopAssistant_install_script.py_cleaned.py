import sys
import os
from setuptools.command.install import install
project_name = "kdDesktopAssistant"
class InstallCmd(install):
    def run(self):
        install.run(self)
        try:
            if sys.platform == "win32":
                script_file = os.path.join(self._get_desktop_folder(), project_name + '.bat')
                with open(script_file, "w") as f:
                    f.write("@echo off\r\nstart " + project_name + ".exe")
            elif sys.platform == "linux":
                script_file = os.path.join(self._get_desktop_folder(), project_name + '.sh')
                with open(script_file, "w") as f:
                    f.write("
                    f.write(project_name + ".exe &")
                    st = os.stat(script_file)
                    os.chmod(script_file, st.st_mode | 0o111)
        except Exception as e:
            print("Cannot create start script: " + str(e))
    def _get_desktop_folder(self):
        try:
            return os.path.join(os.path.expanduser('~'), 'Desktop')
        except Exception:
            return ""
if __name__ == "__main__":
    install_cmd = InstallCmd()
    install_cmd.run()