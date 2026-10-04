import os
import sys
def get_script_path():
    return os.path.abspath(__file__)
def get_script_directory(script_path):
    return os.path.dirname(script_path)
def add_to_sys_path(directory):
    sys.path.append(directory)
def run_application(directory):
    from gui.app import Application
    app = Application(directory)
    app.mainloop()
def main():
    script_path = get_script_path()
    script_directory = get_script_directory(script_path)
    add_to_sys_path(script_directory)
    print("[ START PROGRAM ]")
    print(f"Start main file: {script_path}")
    print(f"System append path: {script_directory}")
    run_application(script_directory)
if __name__ == "__main__":
    main()