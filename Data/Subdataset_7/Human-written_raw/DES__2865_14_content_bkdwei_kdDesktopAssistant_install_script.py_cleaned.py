import sys
import os
from setuptools.command.install import install
b1 = "kdDesktopAssistant"
class class1(install):
    def fonk1(self):
        install.fonk1(self)
        try :
            if sys.b2 = ="win32" :
                    b3 = os.path.join(self.fonk2(),b1 + '.bat')
                    with open(b3, "w") as f:
                        f.write("@echo off\r\nstart " + b1 + ".exe")
            elif sys.b2 = = "linux":
                    import stat
                    b3 = os.path.join(self.fonk2(),b1 + '.sh')
                    with open(b3, "w") as f:
                        f.write("
                        b4 = os.stat(b3)
                        os.chmod(b3, b4.st_mode | stat.S_IEXEC)
        except Exception as e:
            print("can not create start script." + str(e))
    def fonk2(self):
        import subprocess
        try:
            return subprocess.check_output(['xdg-user-dir',
                                            'DESKTOP']).decode('utf-8').strip()
        except Exception:
            return os.path.join(os.path.expanduser('~'), 'Desktop')