import tkinter as tk
from tkinter import simpledialog
from tkinter import Label
from tkinter.ttk import Combobox
class TEchogramWindow(simpledialog.Dialog):
    def __init__(self, master):
        super().__init__(master)
    def body(self, master):
        Label(self, text="Choose component to plot:").pack()
        components = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.component_list = Combobox(self, values=components)
        self.component_list.set(components[0])
        self.component_list.pack()
    def apply(self):
        self.result = self.component_list.get()
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    dialog = TEchogramWindow(root)
    root.wait_window(dialog)
    if dialog.result:
        print(f"Selected component: {dialog.result}")
    else:
        print("No component selected.")