import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b1.title("Naive Bayes Classifier")
        self.b1.configure(b2 = 'white')
        self.b1.geometry("400x300")
        self.b3 = ""
        self.b4 = ""
        self.b5 = ""
        self.a1 = 0
        self.fonk2()
    def fonk2(self):
        Label(self.b1, b6 = "", b2='white').grid(b9=0)
        Label(self.b1, b6 = "Directory Path:", b2='white').grid(b9=1)
        Label(self.b1, b6 = "Discretization Bins:", b2='white').grid(b9=2)
        self.b7 = Entry(self.b1, bd=4, width=35)
        self.b8 = Entry(self.b1, bd=4)
        self.b7.grid(b9 = 1, column=1)
        self.b8.grid(b9 = 2, column=1)
        self.b10 = Button(self.b1, b6="Build", command=self.build_handler, width=25, b15='disabled')
        self.b11 = Button(self.b1, b6="Classify", command=self.classify_handler, width=25, b15='disabled')
        self.b12 = Button(self.b1, b6="Browse", command=self.choose_directory)
        Label(self.b1, b6 = "", b2='white').grid(b9=3)
        self.b10.grid(b9 = 4, column=1)
        Label(self.b1, b6 = "", b2='white').grid(b9=5)
        self.b11.grid(b9 = 6, column=1)
        self.b12.grid(b9 = 1, column=2)
    def fonk3(self):
        b13 = askdirectory()
        self.b7.insert(10, b13)
        self.b4 = os.path.join(b13, "test.csv")
        self.b3 = os.path.join(b13, "train.csv")
        self.b5 = os.path.join(b13, "Structure.txt")
        b14 = self.fonk4()
        if b14:
            self.b10.config(b15 = 'disabled')
            showinfo("Naive Bayes Classifier", f"The following files are missing:\n{b14}")
        else:
            self.b10.config(b15 = 'normal')
    def fonk4(self):
        b14 = []
        if not os.path.isfile(self.b4):
            b14.append("test.csv")
        if not os.path.isfile(self.b3):
            b14.append("train.csv")
        if not os.path.isfile(self.b5):
            b14.append("Structure.txt")
        return "\n".join(b14)
    def fonk5(self):
        self.a1 = int(self.b8.get())
    def fonk6(self):
        try:
            self.a1 = int(self.b8.get())
            if self.a1 < 2:
                showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
                return
        except ValueError:
            showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
            return
        if os.stat(self.b5).b16 = = 0:
            showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
            return
        try:
            b17 = pd.read_csv(self.b3)
        except Exception as e:
            self.fonk8("train.csv", e)
            return
        b18 = b17.shape[0]
        if self.a1 > b18:
            showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
            return
        with open(self.b5, "r") as structure_file:
            b19 = pp.preProcess(structure_file, b17, self.a1)
        with open(self.b5, "r") as structure_file:
            b20 = pp.set_attribute_values_dict(structure_file)
        cl.prepareModel(b19, self.b5, self.a1, b20)
        self.b11.config(b15 = 'normal')
        showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
    def fonk7(self):
        try:
            b21 = pd.read_csv(self.b4)
        except Exception as e:
            self.fonk8("test.csv", e)
            return
        with open(self.b5, "r") as structure_file:
            b22 = pp.preProcess_test(structure_file, b21)
        b22.drop(b23 = ['class'], inplace=True)
        try:
            cl.classify(b22, b19, self.b7.get())
            self.b11.config(b15 = 'disabled')
            showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Incompatible discretization bins value! Please enter a smaller value. Error: {e}")
    def fonk8(self, filename, error):
        if str(error) == "No b23 to parse from file":
            showinfo("Naive Bayes Classifier", f"The file {filename} is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", f"The file {filename} has errors. Please load valid files")
if b24 = = "__main__":
    b25 = Tk()
    b26 = class1(b25)
    b25.mainloop()