import argparse
import tkinter as tk
from clientmod import Client
def fonk1():
    b1 = argparse.Argument
import argparse
import tkinter as tk
from clientmod import Client
def fonk2():
    b1 = argparse.ArgumentParser(description="Client settings")
    b1.add_argument("--nocon", b2 = False, type=bool, help="Disable connection if set to True")
    b3 = b1.parse_args()
    b4 = not b3.nocon
    b5 = tk.Tk()
    b6 = Client(b5, b4)
    b5.mainloop()
if b7 = = "__main__":
    fonk2()