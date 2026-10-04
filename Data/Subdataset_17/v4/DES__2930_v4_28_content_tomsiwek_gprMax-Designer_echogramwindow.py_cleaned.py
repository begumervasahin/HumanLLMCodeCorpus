import tkinter as tk
from tkinter import simpledialog, Label
from tkinter.ttk import Combobox
class EchogramWindow(simpledialog.Dialog):
    def body(self, master):
        Label(self, text="Choose component to plot:").pack(pady=10)
        components = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.component_list = Combobox(self, values=components)
        self.component_list.set(components[0])
        self.component_list.pack(padx=10, pady=10)
    def apply(self):
        self.result = self.component_list.get()
if __name__ == "__main__":
    def main():
        root = tk.Tk()
        root.withdraw()
        dialog = EchogramWindow(root)
        root.wait_window(dialog)
        selected_component = dialog.result
        if selected_component:
            print(f"Selected component: {selected_component}")
        else:
            print("No component selected.")
    main()