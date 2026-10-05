import sys
import tkinter as tk
from tkinter import simpledialog
class PlotParam(simpledialog.Dialog):
    def body(self, master):
        self.title('Enter new plot parameters...')
        labels = ['Min X:', 'Max X:', 'Bin width:', 'Max Y:']
        self.entries = []
        for i, label_text in enumerate(labels):
            label = tk.Label(master, text=label_text)
            label.grid(row=i, column=0, sticky=tk.W)
            entry = tk.Entry(master, justify=tk.CENTER)
            entry.grid(row=i, column=1)
            entry.insert(tk.END, '0' if i == 0 else '10' if i == 1 else '1' if i == 2 else '1000')
            self.entries.append(entry)
        return self.entries[0]
    def apply(self):
        self.x_min = int(self.entries[0].get())
        self.x_max = int(self.entries[1].get())
        self.bin_width = int(self.entries[2].get())
        self.y_max = int(self.entries[3].get())
if __name__ == "__main__":
    root = tk.Tk()
    dialog = PlotParam(root)
    print("Min X:", dialog.x_min)
    print("Max X:", dialog.x_max)
    print("Bin width:", dialog.bin_width)
    print("Max Y:", dialog.y_max)
    root.mainloop()