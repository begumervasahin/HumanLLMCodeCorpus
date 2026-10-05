import sys
import os
from setuptools.command.install import install
PROJECT_NAME = "kdDesktopAssistant"
class InstallCmd(install):
    def run(self):
        install.run(self)
        try:
            if sys.platform == "win32":
                self._create_windows_startup_script()
            elif sys.platform == "linux":
                self._create_linux_startup_script()
        except Exception as e:
            print(f"Failed to create the startup script: {e}")
    def _create_windows_startup_script(self):
        script_file = os.path.join(self._get_desktop_folder(), f"{PROJECT_NAME}.bat")
        with open(script_file, "w") as f:
            f.write("@echo off\r\nstart " + f"{PROJECT_NAME}.exe")
    def _create_linux_startup_script(self):
        script_file = os.path.join(self._get_desktop_folder(), f"{PROJECT_NAME}.sh")
        with open(script_file, "w") as f:
            f.write("
            f.write(f"{PROJECT_NAME}.exe &")
            st = os.stat(script_file)
            os.chmod(script_file, st.st_mode | 0o111)
    def _get_desktop_folder(self):
        try:
            return os.path.join(os.path.expanduser('~'), 'Desktop')
        except Exception:
            return ""