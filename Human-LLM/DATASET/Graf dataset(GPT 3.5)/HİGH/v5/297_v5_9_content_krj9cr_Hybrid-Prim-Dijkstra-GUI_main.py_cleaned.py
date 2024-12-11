import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
from App import App
def fonk1():
    b1 = tk.Tk()
    b1.wm_title("Prim & Dijkstra's Algorithms")
    b2 = App(b1)
    b1.mainloop()
if b3 = = "__main__":
    fonk1()