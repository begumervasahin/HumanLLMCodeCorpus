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
        Label(self.b1, b6 = "", b2='white').grid(b8=0)
        Label(self.b1, b6 = "Directory Path:", b2='white').grid(b8=1)
        Label(self.b1, b6 = "Discretization Bins:", b2='white').grid(b8=2)
        self.b7 = Entry(self.b1, bd=4, width=35)
        self.b7.grid(b8 = 1, column=1)
        self.b9 = Entry(self.b1, bd=4)
        self.b9.grid(b8 = 2, column=1)
        Label(self.b1, b6 = "", b2='white').grid(b8=3)
        self.b10 = Button(self.b1, b6="Build", command=self.build_handler, width=25, b15=DISABLED)
        self.b10.grid(b8 = 4, column=1)
        Label(self.b1, b6 = "", b2='white').grid(b8=5)
        self.b11 = Button(self.b1, b6="Classify", command=self.classify_handler, width=25, b15=DISABLED)
        self.b11.grid(b8 = 6, column=1)
        b12 = Button(self.b1, b6="Browse", command=self.choose_directory)
        b12.grid(b8 = 1, column=2)
    def fonk3(self):
        b13 = askdirectory()
        self.b7.insert(10, b13)
        self.b3 = os.path.join(b13, "train.csv")
        self.b4 = os.path.join(b13, "test.csv")
        self.b5 = os.path.join(b13, "Structure.txt")
        b14 = self.fonk4()
        if b14:
            self.b10.config(b15 = DISABLED)
            showinfo("Naive Bayes Classifier", "The following files are missing:\n" + "\n".join(b14))
        else:
            self.b10.config(b15 = NORMAL)
    def fonk4(self):
        b14 = []
        for file_path in [self.b3, self.b4, self.b5]:
            if not os.path.exists(file_path):
                b14.append(os.path.basename(file_path))
        return b14
    def fonk5(self):
        try:
            b16 = int(self.b9.get())
            if b16 < 2:
                showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
                return
        except ValueError:
            showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
            return
        if os.stat(self.b5).b17 = = 0:
            showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
            return
        try:
            b18 = pd.read_csv(self.b3)
            b19 = b18.shape[0]
            if b16 > b19:
                showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
                return
            with open(self.b5, "r") as structure_file:
                b20 = pp.preProcess(structure_file, b18, b16)
                b21 = pp.set_attribute_values_dict(structure_file)
                cl.prepareModel(b20, self.b5, b16, b21)
            self.b11.config(b15 = NORMAL)
            showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
    def fonk6(self):
        try:
            b22 = pd.read_csv(self.b4)
            with open(self.b5, "r") as structure_file:
                b23 = pp.preProcess_test(structure_file, b22)
                b23.drop(b24 = ['class'], inplace=True)
                cl.classify(b23, b20, b13)
                self.b11.config(b15 = DISABLED)
                showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
if b25 = = "__main__":
    b26 = Tk()
    b27 = class1(b26)
    b26.mainloop()