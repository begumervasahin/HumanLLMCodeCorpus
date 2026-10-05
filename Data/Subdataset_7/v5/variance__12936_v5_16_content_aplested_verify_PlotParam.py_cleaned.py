import sys
if sys.version_info[0] < 3:
    from Tkinter import Tk, Label, Entry, END, CENTER
    import tkSimpleDialog as simpledialog
else:
    from tkinter import Tk, Label, Entry, END, CENTER
    from tkinter import simpledialog
b1 = "remis"
b2 = "27-May-2009"
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master, b3 = 'Enter New Plot Parameters')
    def fonk2(self, master):
        b4 = [('Min X:', '0'), ('Max X:', '10'), ('Bin width:', '1'), ('Max Y:', '1000')]
        self.b5 = {}
        for idx, (label, default) in enumerate(b4):
            Label(master, b6 = label).grid(b8=idx, sticky=W)
            b7 = Entry(master, justify=CENTER)
            b7.grid(b8 = idx, column=1)
            b7.insert(END, default)
            self.b5[label] = b7
        return self.b5['Min X:']
    def fonk3(self):
        try:
            self.b4 = {
                'xmin': int(self.b5['Min X:'].get()),
                'xmax': int(self.b5['Max X:'].get()),
                'dx': int(self.b5['Bin width:'].get()),
                'ymax': int(self.b5['Max Y:'].get())
            }
        except ValueError:
            print("Please enter valid integer values.")
            return
if b9 = = "__main__":
    b10 = Tk()
    b10.withdraw()
    b11 = class1(b10)
    print(b11.b4)
