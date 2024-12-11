import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from tkinter import *
from tkFileDialog import askdirectory
from tkMessageBox import showinfo
b1 = ""
b2 = ""
b3 = ""
def fonk1():
    global b4, b1, b2, b3
    b4 = askdirectory()
    b18.insert(10, b4)
    b2 = os.path.join(b4, "test.csv")
    b1 = os.path.join(b4, "train.csv")
    b3 = os.path.join(b4, "Structure.txt")
    fonk5()
def fonk2():
    global b5
    try:
        b5 = int(b20.get())
    except ValueError:
        showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
def fonk3():
    fonk2()
    if not fonk5():
        return
    b6 = pd.read_csv(b1)
    b7 = b6.shape[0]
    if b5 < 2:
        showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
        return
    if b5 > b7:
        showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
        return
    b8 = open(b3, "r")
    b9 = pp.preProcess(b8, b6, b5)
    b10 = pp.set_attribute_values_dict(b8)
    cl.prepareModel(b9, b3, b5, b10)
    b23.config(b11 = 'normal')
    showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
def fonk4():
    if not fonk5():
        return
    b12 = pd.read_csv(b2)
    b8 = open(b3, "r")
    b13 = pp.preProcess_test(b8, b12)
    b13.__delitem__('class')
    try:
        cl.classify(b13, b9, b4)
        b23.config(b11 = 'disabled')
        showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
    except Exception as e:
        showinfo("Naive Bayes Classifier", "Incompatible discretization bins value! Please enter a smaller value")
def fonk5():
    global b1, b2, b3
    a1 = 0
    b14 = "The following files are missing:\n"
    if not os.path.exists(b1):
        a1 = 1
        b14 += "train.csv\n"
    if not os.path.exists(b2):
        a1 = 1
        b14 += "test.csv\n"
    if not os.path.exists(b3):
        a1 = 1
        b14 += "Structure.txt\n"
    if a1:
        b22.config(b11 = 'disabled')
        showinfo("Naive Bayes Classifier", b14)
        return False
    else:
        return True
b15 = Tk()
b15.wm_title("Naive Bayes Classifier")
b15.configure(b16 = 'white')
b15.geometry("400x300")
Label(b15, b17 = "", b16='white').grid(b21=0)
Label(b15, b17 = "Directory Path:", b16='white').grid(b21=1)
Label(b15, b17 = "Discretization Bins:", b16='white').grid(b21=2)
b18 = Entry(b15)
b18.configure(b19 = 4, width=35)
b20 = Entry(b15)
b20.configure(b19 = 4)
b18.grid(b21 = 1, column=1)
b20.grid(b21 = 2, column=1)
Label(b15, b17 = "", b16='white').grid(b21=3)
b22 = Button(b15, b17="Build", command=build_handler, width=25)
b23 = Button(b15, b17="Classify", command=classify_handler, width=25)
b24 = Button(b15, b17="Browse", command=choose_directory)
b22.grid(b21 = 4, column=1)
b23.grid(b21 = 6, column=1)
b24.grid(b21 = 1, column=2)
b23.config(b11 = 'disabled')
Label(b15, b17 = "", b16='white').grid(b21=5)
mainloop()