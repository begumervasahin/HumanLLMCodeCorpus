from uncompyle6.main import decompile
import marshal
import sys
import os
import marcode
def decompile_and_save(py_version, output_file, marcode_data):
    try:
        code_obj = marshal.loads(marcode_data)
        decompiled_code = decompile(py_version, code_obj, sys.stdout)
        with open(f"{output_file}.py", "w") as f:
            f.write(decompiled_code)
        print(f"\n\n[result] Saved as \033[95m{output_file}.py")
    except Exception as e:
        print(f"Error: {e}")
def decompile_python3():
    output_file = input("[*] Decompile marshal Python 3.7.X\n[?] File output: ")
    decompile_and_save(3.7, output_file, marcode.py3)
def decompile_python2():
    output_file = input("[*] Decompile marshal Python 2.7.X\n[?] File output: ")
    decompile_and_save(2.7, output_file, marcode.py2)
def main():
    try:
        os.system('clear')
        print()
        if sys.version_info[0] == 3:
            decompile_python3()
        elif sys.version_info[0] == 2:
            decompile_python2()
        else:
            print("Unsupported Python version.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()