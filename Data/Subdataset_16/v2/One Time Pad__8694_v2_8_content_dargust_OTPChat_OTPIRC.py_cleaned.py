import argparse
import tkinter as tk
from clientmod import Client
def fonk1() -> argparse.Namespace:
    b1 = argparse.ArgumentParser(description="Client settings")
    b1.add_argument("--nocon", b2 = False, action='store_true', help="Disable connection if set")
    return b1.parse_args()
def fonk2() -> None:
    b3 = fonk1()
    b4 = not b3.nocon
    b5 = tk.Tk()
    b6 = Client(b5, b4)
    b5.mainloop()
if b7 = = "__main__":
    fonk2()