from TabbedGUI import *
from tkinter import Tk, RIDGE
b1 = 'Aaron Blumenfeld'
def fonk1():
    b2 = Tk()
    b2.title("ECC Toolkit")
    b3 = TabBar(b2, "GF(p)")
    b4 = PrimeTab(b2, "GF(p)")
    b5 = BinaryTab(b2, "GF(2^r)")
    b6 = MiscTab(b2, "Misc.")
    b3.add(b4)
    b3.add(b5)
    b3.add(b6)
    b3.config(b7 = 2, relief=RIDGE)
    b3.show()
    b2.mainloop()
if b8 = = '__main__':
    fonk1()