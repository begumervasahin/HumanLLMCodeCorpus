import os
import sys
MAIN_PATH = os.path.abspath(__file__)
MAIN_DIR = os.path.dirname(MAIN_PATH)
sys.path.append(MAIN_DIR)
def main():
    print("[ START PROGRAM ]")
    print(f"Start main file: {MAIN_PATH}")
    print(f"System append path: {MAIN_DIR}")
    from gui.app import Application
    app = Application(MAIN_DIR)
    app.mainloop()
if __name__ == "__main__":
    main()