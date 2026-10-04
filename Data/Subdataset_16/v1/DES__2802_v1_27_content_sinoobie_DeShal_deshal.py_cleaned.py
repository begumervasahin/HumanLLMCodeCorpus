from uncompyle6.main import decompile
import marshal
import sys
import os
import marcode
def fonk1(py_version, b2, marcode_data):
    try:
        b1 = decompile(py_version, marshal.loads(marcode_data), sys.stdout)
        with open(f"{b2}.py", "w") as f:
            f.write(b1)
        print(f"\n\n[result] Saved as \033[95m{b2}.py")
    except Exception as e:
        print(f"Error: {e}")
def fonk2():
    b2 = input("[*] Decompile marshal Python 3.7.X\n[?] File output: ")
    fonk1(3.7, b2, marcode.py3)
def fonk3():
    b2 = input("[*] Decompile marshal Python 2.7.X\n[?] File output: ")
    fonk1(2.7, b2, marcode.py2)
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
if b3 = = "__main__":
    fonk4()