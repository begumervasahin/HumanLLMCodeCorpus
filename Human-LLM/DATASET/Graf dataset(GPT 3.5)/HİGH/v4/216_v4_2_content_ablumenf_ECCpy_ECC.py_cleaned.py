from tkinter import Tk, RIDGE
from TabbedGUI import TabBar, PrimeTab, BinaryTab, MiscTab
def fonk1():
    b1 = Tk()
    b1.title("ECC Toolkit")
    b2 = TabBar(b1, "GF(p)")
    b3 = PrimeTab(b1, "GF(p)")
    b4 = BinaryTab(b1, "GF(2^r)")
    b5 = MiscTab(b1, "Miscellaneous")
    b2.add(b3)
    b2.add(b4)
    b2.add(b5)
    b2.config(b6 = 2, relief=RIDGE)
    b2.show()
    b1.mainloop()
if b7 = = "__main__":
    fonk1()