import os
import sys
def get_main_path():
    return os.path.abspath(__file__)
def get_main_dir(main_path):
    return os.path.dirname(main_path)
def append_sys_path(main_dir):
    sys.path.append(main_dir)
def initialize_app(main_dir):
    from gui.app import Application
    app = Application(main_dir)
    app.mainloop()
def main():
    main_path = get_main_path()
    main_dir = get_main_dir(main_path)
    append_sys_path(main_dir)
    print("[ START PROGRAM ]")
    print(f"Start main file: {main_path}")
    print(f"System append path: {main_dir}")
    initialize_app(main_dir)
if __name__ == "__main__":
    main()