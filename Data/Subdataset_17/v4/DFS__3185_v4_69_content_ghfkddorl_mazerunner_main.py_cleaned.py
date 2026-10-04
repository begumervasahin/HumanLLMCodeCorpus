import os
import sys
from gui.app import Application
def setup_environment():
    script_path = os.path.abspath(__file__)
    script_directory = os.path.dirname(script_path)
    sys.path.append(script_directory)
    return script_path, script_directory
def main():
    script_path, script_directory = setup_environment()
    print("[ START PROGRAM ]")
    print(f"Start main file: {script_path}")
    print(f"System path appended: {script_directory}")
    app = Application(script_directory)
    app.mainloop()
if __name__ == "__main__":
    main()