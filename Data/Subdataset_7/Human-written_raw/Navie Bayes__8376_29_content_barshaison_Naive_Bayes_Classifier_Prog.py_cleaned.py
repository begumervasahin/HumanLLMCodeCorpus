import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from Tkinter import *
from tkFileDialog import askdirectory
from tkMessageBox import *
b1 = ""
b2 = ""
b3 = ""
b4 = Tk()
b4.wm_title("Naive Bayes Classifier")
b4.configure(b5 = 'white')
b4.geometry("400x300")
Label(b4,b6 = "",b5='white').grid(b26=0)
Label(b4, b6 = "Directory Path:",b5='white').grid(b26=1)
Label(b4, b6 = "Discretization Bins:",b5='white').grid(b26=2)
b7 = Entry(b4)
b7.configure(b8 = 4,width=35)
b9 = Entry(b4)
b9.configure(b8 = 4)
a1 = 0
def fonk1():
    global b10
    b10 = askdirectory()
    b7.insert(10,b10)
    global b1
    global b2
    global b3
    b2 = b10 + "/test.csv"
    b1 = b10 + "/train.csv"
    b3 = b10 + "/Structure.txt"
    global a1
    a1 = 0
    b11 = "The following files are missing:\n"
    try:
        b12 = open(b2)
    except IOError as e:
        a1 = 1
        b11 += "test.csv\n"
    try:
        b12 = open(b1)
    except IOError as e:
        a1 = 1
        b11 += "train.csv\n"
    try:
        b12 = open(b3)
    except IOError as e:
        a1 = 1
        b11 += "Structure.txt\n"
    if a1 = = 1:
        b24.config(b13 = 'disabled')
        showinfo("Naive Bayes Classifier",b11)
    else:
        b24.config(b13 = 'normal')
def fonk2():
    global b14
    b14 = int(b9.get())
def fonk3():
    try:
        global b14
        b15 = b9.get()
        if b15 = = "":
            showinfo("Naive Bayes Classifier", "Please insert an integer for the Discretization bins attribute")
            return
        b14 = int(b15)
    except:
        showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
        return
    if b14 < 2:
        showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
        return
    if os.stat(b3).b16 = = 0:
        showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
        return
    b17 = open(b3, "r")
    try:
        b18 = pd.read_csv(b1)
    except Exception as e:
        if e.__str__() == "No columns to parse from file":
            showinfo("Naive Bayes Classifier", "The file train.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file train.csv has errors. Please load valid files")
    b19 = b18.shape[0]
    if b14 > b19:
        showinfo("Naive Bayes Classifier", "Discretization bins must not be grater than the number of train set records")
        return
    global b20
    b20 = pp.preProcess(b17, b18, b14)
    b17 = open(b3, "r")
    b21 = pp.set_attribute_values_dict(b17)
    cl.prepareModel(b20, b3, b14,b21)
    b25.config(b13 = 'normal')
    showinfo("Naive Bayes Classifier","Building classifier using train-set is done!")
def fonk4():
    try:
        b22 = pd.read_csv(b2)
    except Exception as e:
        if e.__str__() == "No columns to parse from file":
            showinfo("Naive Bayes Classifier", "The file test.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file test.csv has errors. Please load valid files")
    b17 = open(b3, "r")
    b23 = pp.preProcess_test(b17, b22)
    b23.__delitem__('class')
    try:
        cl.classify(b23, b20, b10)
        b25.config(b13 = 'disabled')
        showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
    except Exception as e:
        showinfo("Naive Bayes Classifier", "Incompatibale discretization bins value! Please enter smaller value ")
b24 = Button(b4, b6="Build", command=build_handler,width=25)
b25 = Button(b4, b6="Classify", command=classify_handler,width=25)
b7.grid(b26 = 1, column=1)
b9.grid(b26 = 2, column=1)
Label(b4,b6 = "",b5='white').grid(b26=3)
b24.grid(b26 = 4,column=1)
b24.config(b13 = 'disabled')
Label(b4,b6 = "",b5='white').grid(b26=5)
b25.grid(b26 = 6,column=1)
b25.config(b13 = 'disabled')
b27 = Button(b4, b6="Browse", command=choose_directory)
b27.grid(b26 = 1,column=2)
mainloop()