from uncompyle6.main import decompile
import marshal
import sys
import os
import marcode
def decompile_and_save(py_version, output_file, marcode_data):
    try:
        decompiled_code = decompile(py_version, marshal.loads(marcode_data), sys.stdout)
        with open(f"{output_file}.py", "w") as f:
            f.write(decompiled_code)
        print(f"\n\n[result] Saved as \033[95m{output_file}.py")
    except Exception as e:
        print(f"Error: {e}")
def py3():
    output_file = input("[*] Decompile marshal Python 3.7.X\n[?] File output: ")
    decompile_and_save(3.7, output_file, marcode.py3)
def py2():
    output_file = input("[*] Decompile marshal Python 2.7.X\n[?] File output: ")
    decompile_and_save(2.7, output_file, marcode.py2)
def main():
    try:
        os.system('clear')
        print()
        if sys.version_info[0] == 3:
            py3()
        elif sys.version_info[0] == 2:
            py2()
        else:
            print("Unsupported Python version.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    main()