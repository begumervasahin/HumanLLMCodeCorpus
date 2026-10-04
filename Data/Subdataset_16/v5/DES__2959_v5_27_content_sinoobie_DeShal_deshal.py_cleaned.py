import marshal
import os
import sys
from uncompyle6.main import decompile
import marcode
def fonk1(py_version, b3, marcode_data):
    try:
        b1 = marshal.loads(marcode_data)
        b2 = decompile(py_version, b1, sys.stdout)
        with open(f"{b3}.py", "w") as f:
            f.write(b2.text)
        print(f"\n\n[result] Saved as \033[95m{b3}.py")
    except Exception as e:
        print(f"Error: {e}")
def fonk2():
    b3 = input("[*] Decompile marshal Python 3.7.X\n[?] File output: ")
    fonk1(3.7, b3, marcode.py3)
def fonk3():
    b3 = input("[*] Decompile marshal Python 2.7.X\n[?] File output: ")
    fonk1(2.7, b3, marcode.py2)
def fonk4():
    try:
        os.system('clear')
        print()
        if sys.version_info[0] == 3:
            fonk2()
        elif sys.version_info[0] == 2:
            fonk3()
        else:
            print("Unsupported Python version.")
    except Exception as e:
        print(f"Error: {e}")
if b4 = = "__main__":
    fonk4()