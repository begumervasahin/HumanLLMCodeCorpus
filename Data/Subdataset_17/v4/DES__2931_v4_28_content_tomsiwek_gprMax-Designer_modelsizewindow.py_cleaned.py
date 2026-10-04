import tkinter as tk
from tkinter import simpledialog, Label, Entry
class ModelSizeWindow(simpledialog.Dialog):
    def __init__(self, master):
        super().__init__(master)
    def body(self, master):
        Label(master, text="x:").grid(row=0, column=0, padx=10, pady=5)
        Label(master, text="y:").grid(row=1, column=0, padx=10, pady=5)
        self.x_entry = Entry(master)
        self.y_entry = Entry(master)
        self.x_entry.grid(row=0, column=1, padx=10, pady=5)
        self.y_entry.grid(row=1, column=1, padx=10, pady=5)
    def apply(self):
        self.result = (self.x_entry.get(), self.y_entry.get())
def main():
    root = tk.Tk()
    root.withdraw()
    dialog = ModelSizeWindow(root)
    root.wait_window(dialog)
    if dialog.result:
        x, y = dialog.result
        print(f"Model size: x={x}, y={y}")
    else:
        print("No model size entered.")
if __name__ == "__main__":
    main()