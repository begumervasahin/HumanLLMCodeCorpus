import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from App import *
def main():
    root = Tk.Tk()
    root.wm_title("Prim & Dijkstra's Algorithms")
    app = App(root)
    Tk.mainloop()
if __name__ == "__main__":
    main()