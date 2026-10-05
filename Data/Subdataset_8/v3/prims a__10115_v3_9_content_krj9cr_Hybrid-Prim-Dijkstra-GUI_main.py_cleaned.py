import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
from App import App
def main():
    root = Tk.Tk()
    root.title("Prim & Dijkstra's Algorithms")
    app = App(root)
    root.mainloop()
if __name__ == "__main__":
    main()