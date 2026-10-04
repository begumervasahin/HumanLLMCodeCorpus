from TabbedGUI import *
from tkinter import Tk, RIDGE
b1 = 'Aaron Blumenfeld'
def fonk1():
    b2 = Tk()
    b2.title("ECC Toolkit")
    b3 = TabBar(b2, "GF(p)")
    b3.config(b4 = 2, relief=RIDGE)
    b5 = PrimeTab(b2, "GF(p)")
    b6 = BinaryTab(b2, "GF(2^r)")
    b7 = MiscTab(b2, "Misc.")
    b3.add(b5)
    b3.add(b6)
    b3.add(b7)
    b3.show()
    b2.mainloop()
if b8 = = '__main__':
    fonk1()