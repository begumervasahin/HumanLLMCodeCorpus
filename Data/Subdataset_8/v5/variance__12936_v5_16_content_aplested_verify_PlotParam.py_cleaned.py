import sys
if sys.version_info[0] < 3:
    from Tkinter import Tk, Label, Entry, END, CENTER
    import tkSimpleDialog as simpledialog
else:
    from tkinter import Tk, Label, Entry, END, CENTER
    from tkinter import simpledialog
__author__ = "remis"
__date__ = "27-May-2009"
class PlotParameterDialog(simpledialog.Dialog):
    def __init__(self, master):
        super().__init__(master, title='Enter New Plot Parameters')
    def body(self, master):
        parameters = [('Min X:', '0'), ('Max X:', '10'), ('Bin width:', '1'), ('Max Y:', '1000')]
        self.entries = {}
        for idx, (label, default) in enumerate(parameters):
            Label(master, text=label).grid(row=idx, sticky=W)
            entry_widget = Entry(master, justify=CENTER)
            entry_widget.grid(row=idx, column=1)
            entry_widget.insert(END, default)
            self.entries[label] = entry_widget
        return self.entries['Min X:']
    def apply(self):
        try:
            self.parameters = {
                'xmin': int(self.entries['Min X:'].get()),
                'xmax': int(self.entries['Max X:'].get()),
                'dx': int(self.entries['Bin width:'].get()),
                'ymax': int(self.entries['Max Y:'].get())
            }
        except ValueError:
            print("Please enter valid integer values.")
            return
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    dialog = PlotParameterDialog(root)
    print(dialog.parameters)
