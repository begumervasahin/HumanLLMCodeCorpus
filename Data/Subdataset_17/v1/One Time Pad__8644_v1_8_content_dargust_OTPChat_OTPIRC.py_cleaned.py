import argparse
import tkinter as tk
from clientmod import Client
def main():
    parser = argparse.Argument
import argparse
import tkinter as tk
from clientmod import Client
def main():
    parser = argparse.ArgumentParser(description="Client settings")
    parser.add_argument("--nocon", default=False, type=bool, help="Disable connection if set to True")
    args = parser.parse_args()
    connect = not args.nocon
    root = tk.Tk()
    client = Client(root, connect)
    root.mainloop()
if __name__ == "__main__":
    main()