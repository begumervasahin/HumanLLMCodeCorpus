import argparse
import tkinter as tk
from clientmod import Client
def fonk1():
    b1 = argparse.ArgumentParser(description="Client settings")
    b1.add_argument("--nocon", b2 = "store_true", help="Disable connection")
    return b1.parse_args()
def fonk2(b6):
    b3 = tk.Tk()
    b4 = Client(b3, b6)
    b3.mainloop()
def fonk3():
    b5 = fonk1()
    b6 = not b5.nocon
    fonk2(b6)
if b7 = = '__main__':
    fonk3()