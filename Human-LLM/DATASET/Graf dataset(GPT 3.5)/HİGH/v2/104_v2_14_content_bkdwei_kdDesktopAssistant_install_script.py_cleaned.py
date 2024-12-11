import sys
import os
from setuptools.command.install import install
b1 = "kdDesktopAssistant"
class class1(install):
    def fonk1(self):
        install.fonk1(self)
        try:
            if sys.b2 = = "win32":
                b3 = os.path.join(self.fonk2(), b1 + '.bat')
                with open(b3, "w") as f:
                    f.write("@echo off\r\nstart " + b1 + ".exe")
            elif sys.b2 = = "linux":
                b3 = os.path.join(self.fonk2(), b1 + '.sh')
                with open(b3, "w") as f:
                    f.write("
                    f.write(b1 + ".exe &")
                    b4 = os.stat(b3)
                    os.chmod(b3, b4.st_mode | 0o111)
        except Exception as e:
            print("Cannot create start script: " + str(e))
    def fonk2(self):
        try:
            return os.path.join(os.path.expanduser('~'), 'Desktop')
        except Exception:
            return ""
if b5 = = "__main__":
    b6 = class1()
    b6.fonk1()