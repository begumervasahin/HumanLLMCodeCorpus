import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from App import App
def fonk1():
    b1 = Tk.Tk()
    b1.title("Prim & Dijkstra's Algorithms")
    b2 = App(b1)
    b1.mainloop()
if b3 = = "__main__":
    fonk1()