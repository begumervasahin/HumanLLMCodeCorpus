import pandas as pd
import os
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
import PreProcessing as pp
import Classifier as cl
b1 = ""
b2 = ""
b3 = ""
b4 = Tk()
b4.wm_title("Naive Bayes Classifier")
b4.configure(b5 = 'white')
b4.geometry("400x300")
Label(b4, b6 = "", b5='white').grid(b24=0)
Label(b4, b6 = "Directory Path:", b5='white').grid(b24=1)
Label(b4, b6 = "Discretization Bins:", b5='white').grid(b24=2)
b7 = Entry(b4, bd=4, width=35)
b8 = Entry(b4, bd=4)
def fonk1():
    global b1, b2, b3
    b9 = askdirectory()
    b7.insert(10, b9)
    b2 = os.path.join(b9, "test.csv")
    b1 = os.path.join(b9, "train.csv")
    b3 = os.path.join(b9, "Structure.txt")
    check_file_existence()
def fonk2():
    global b10
    b10 = int(b8.get())
def fonk3():
    try:
        fonk2()
    except:
        showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
        return
    if b10 < 2:
        showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
        return
    if os.stat(b3).b11 = = 0:
        showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
        return
    b12 = open(b3, "r")
    try:
        b13 = pd.read_csv(b1)
    except Exception as e:
        if e.__str__() == "No columns to parse from file":
            showinfo("Naive Bayes Classifier", "The file train.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file train.csv has errors. Please load valid files")
    b14 = b13.shape[0]
    if b10 > b14:
        showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
        return
    b15 = pp.preProcess(b12, b13, b10)
    b12 = open(b3, "r")
    b16 = pp.set_attribute_values_dict(b12)
    cl.prepareModel(b15, b3, b10, b16)
    b23.config(b17 = 'normal')
    showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
def fonk4():
    try:
        b18 = pd.read_csv(b2)
    except Exception as e:
        if e.__str__() == "No columns to parse from file":
            showinfo("Naive Bayes Classifier", "The file test.csv is empty. Please load valid files")
        else:
            showinfo("Naive Bayes Classifier", "The file test.csv has errors. Please load valid files")
    b12 = open(b3, "r")
    b19 = pp.preProcess_test(b12, b18)
    b19.drop('class', b20 = 1, inplace=True)
    try:
        cl.classify(b19, b15, b9)
        b23.config(b17 = 'disabled')
        showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
    except Exception as e:
        showinfo("Naive Bayes Classifier", "Incompatible discretization bins value! Please enter smaller value")
b21 = Button(b4, b6="Browse", command=choose_directory)
b22 = Button(b4, b6="Build", command=build_handler, width=25)
b23 = Button(b4, b6="Classify", command=classify_handler, width=25)
b7.grid(b24 = 1, column=1)
b8.grid(b24 = 2, column=1)
Label(b4, b6 = "", b5='white').grid(b24=3)
b22.grid(b24 = 4, column=1)
b22.config(b17 = 'disabled')
Label(b4, b6 = "", b5='white').grid(b24=5)
b23.grid(b24 = 6, column=1)
b23.config(b17 = 'disabled')
b21.grid(b24 = 1, column=2)
mainloop()