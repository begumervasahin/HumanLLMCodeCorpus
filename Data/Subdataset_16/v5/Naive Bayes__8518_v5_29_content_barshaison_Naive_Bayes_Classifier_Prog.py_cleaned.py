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
        b16 = [self.b3, self.b4, self.b5]
        b14 = [os.path.basename(file_path) for file_path in b16 if not os.path.exists(file_path)]
        return b14
    def fonk5(self):
        try:
            b17 = int(self.b9.get())
            if b17 < 2:
                showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
                return
        except ValueError:
            showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
            return
        if os.stat(self.b5).b18 = = 0:
            showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
            return
        try:
            b19 = pd.read_csv(self.b3)
            b20 = b19.shape[0]
            if b17 > b20:
                showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
                return
            with open(self.b5, "r") as structure_file:
                b21 = pp.preProcess(structure_file, b19, b17)
                b22 = pp.set_attribute_values_dict(structure_file)
                cl.prepareModel(b21, self.b5, b17, b22)
            self.b11.config(b15 = NORMAL)
            showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
    def fonk6(self):
        try:
            b23 = pd.read_csv(self.b4)
            with open(self.b5, "r") as structure_file:
                b24 = pp.preProcess_test(structure_file, b23)
                b24.drop(b25 = ['class'], inplace=True)
                cl.classify(b24, b21, self.b7.get())
                self.b11.config(b15 = DISABLED)
                showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
if b26 = = "__main__":
    b27 = Tk()
    b28 = class1(b27)
    b27.mainloop()