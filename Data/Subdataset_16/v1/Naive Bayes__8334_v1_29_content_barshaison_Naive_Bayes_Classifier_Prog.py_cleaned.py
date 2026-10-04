import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
b1 = ""
b2 = ""
b3 = ""
a1 = 0
b4 = Tk()
b4.wm_title("Naive Bayes Classifier")
b4.configure(b5 = 'white')
b4.geometry("400x300")
Label(b4, b6 = "", b5='white').grid(b26=0)
Label(b4, b6 = "Directory Path:", b5='white').grid(b26=1)
Label(b4, b6 = "Discretization Bins:", b5='white').grid(b26=2)
b7 = Entry(b4)
b7.configure(b8 = 4, width=35)
b9 = Entry(b4)
b9.configure(b8 = 4)
def fonk1():
    global b1, b2, b3
    b10 = askdirectory()
    b7.insert(10, b10)
    b2 = os.path.join(b10, "test.csv")
    b1 = os.path.join(b10, "train.csv")
    b3 = os.path.join(b10, "Structure.txt")
    b11 = False
    b12 = "The following files are missing:\n"
    if not os.path.isfile(b2):
        b11 = True
        b12 += "test.csv\n"
    if not os.path.isfile(b1):
        b11 = True
        b12 += "train.csv\n"
    if not os.path.isfile(b3):
        b11 = True
        b12 += "Structure.txt\n"
    if b11:
        b23.config(b13 = 'disabled')
        showinfo("Naive Bayes Classifier", b12)
    else:
        b23.config(b13 = 'normal')
def fonk2():
    global a1
    a1 = int(b9.get())
def fonk3():
    try:
        b14 = b9.get()
        if not b14:
            showinfo("Naive Bayes Classifier", "Please insert an integer for the Discretization bins attribute")
            return
        a1 = int(b14)
    except ValueError:
        showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
        return
    if a1 < 2:
        showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
        return
    if os.stat(b3).b15 = = 0:
        showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
        return
    try:
        b16 = pd.read_csv(b1)
    except Exception as e:
        if str(e) == "No b22 to parse from file":
            showinfo("Naive Bayes Classifier", "The file train.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file train.csv has errors. Please load valid files")
        return
    b17 = b16.shape[0]
    if a1 > b17:
        showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
        return
    with open(b3, "r") as structure_file:
        b18 = pp.preProcess(structure_file, b16, a1)
    with open(b3, "r") as structure_file:
        b19 = pp.set_attribute_values_dict(structure_file)
    cl.prepareModel(b18, b3, a1, b19)
    b24.config(b13 = 'normal')
    showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
def fonk4():
    try:
        b20 = pd.read_csv(b2)
    except Exception as e:
        if str(e) == "No b22 to parse from file":
            showinfo("Naive Bayes Classifier", "The file test.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file test.csv has errors. Please load valid files")
        return
    with open(b3, "r") as structure_file:
        b21 = pp.preProcess_test(structure_file, b20)
    b21.drop(b22 = ['class'], inplace=True)
    try:
        cl.classify(b21, b18, b10)
        b24.config(b13 = 'disabled')
        showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
    except Exception as e:
        showinfo("Naive Bayes Classifier", f"Incompatible discretization bins value! Please enter a smaller value. Error: {e}")
b23 = Button(b4, b6="Build", command=build_handler, width=25)
b24 = Button(b4, b6="Classify", command=classify_handler, width=25)
b25 = Button(b4, b6="Browse", command=choose_directory)
b7.grid(b26 = 1, column=1)
b9.grid(b26 = 2, column=1)
Label(b4, b6 = "", b5='white').grid(b26=3)
b23.grid(b26 = 4, column=1)
b23.config(b13 = 'disabled')
Label(b4, b6 = "", b5='white').grid(b26=5)
b24.grid(b26 = 6, column=1)
b24.config(b13 = 'disabled')
b25.grid(b26 = 1, column=2)
mainloop()