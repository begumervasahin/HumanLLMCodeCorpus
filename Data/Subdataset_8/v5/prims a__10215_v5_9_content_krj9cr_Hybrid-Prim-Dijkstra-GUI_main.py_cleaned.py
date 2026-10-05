import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
from App import App
def run_application():
    root = tk.Tk()
    root.wm_title("Prim & Dijkstra's Algorithms")
    app_instance = App(root)
    root.mainloop()
if __name__ == "__main__":
    run_application()