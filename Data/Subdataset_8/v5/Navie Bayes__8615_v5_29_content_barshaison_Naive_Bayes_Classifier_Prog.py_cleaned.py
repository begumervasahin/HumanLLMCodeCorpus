import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from tkinter import *
from tkFileDialog import askdirectory
from tkMessageBox import showinfo
pathToTrain = ""
pathToTest = ""
pathToStructure = ""
def choose_directory():
    global dir_path, pathToTrain, pathToTest, pathToStructure
    dir_path = askdirectory()
    e1.insert(10, dir_path)
    pathToTest = os.path.join(dir_path, "test.csv")
    pathToTrain = os.path.join(dir_path, "train.csv")
    pathToStructure = os.path.join(dir_path, "Structure.txt")
    check_files()
def set_num_of_bins():
    global numOfIntervals
    try:
        numOfIntervals = int(e2.get())
    except ValueError:
        showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
def build_handler():
    set_num_of_bins()
    if not check_files():
        return
    dfTrain = pd.read_csv(pathToTrain)
    total_num_of_records_train = dfTrain.shape[0]
    if numOfIntervals < 2:
        showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
        return
    if numOfIntervals > total_num_of_records_train:
        showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
        return
    structure_file = open(pathToStructure, "r")
    dfTrainFinal = pp.preProcess(structure_file, dfTrain, numOfIntervals)
    attribute_values_dict = pp.set_attribute_values_dict(structure_file)
    cl.prepareModel(dfTrainFinal, pathToStructure, numOfIntervals, attribute_values_dict)
    classify_Button.config(state='normal')
    showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
def classify_handler():
    if not check_files():
        return
    dfTest = pd.read_csv(pathToTest)
    structure_file = open(pathToStructure, "r")
    dfTestFinal = pp.preProcess_test(structure_file, dfTest)
    dfTestFinal.__delitem__('class')
    try:
        cl.classify(dfTestFinal, dfTrainFinal, dir_path)
        classify_Button.config(state='disabled')
        showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
    except Exception as e:
        showinfo("Naive Bayes Classifier", "Incompatible discretization bins value! Please enter a smaller value")
def check_files():
    global pathToTrain, pathToTest, pathToStructure
    file_missing = 0
    error_string = "The following files are missing:\n"
    if not os.path.exists(pathToTrain):
        file_missing = 1
        error_string += "train.csv\n"
    if not os.path.exists(pathToTest):
        file_missing = 1
        error_string += "test.csv\n"
    if not os.path.exists(pathToStructure):
        file_missing = 1
        error_string += "Structure.txt\n"
    if file_missing:
        build_Button.config(state='disabled')
        showinfo("Naive Bayes Classifier", error_string)
        return False
    else:
        return True
master = Tk()
master.wm_title("Naive Bayes Classifier")
master.configure(background='white')
master.geometry("400x300")
Label(master, text="", background='white').grid(row=0)
Label(master, text="Directory Path:", background='white').grid(row=1)
Label(master, text="Discretization Bins:", background='white').grid(row=2)
e1 = Entry(master)
e1.configure(bd=4, width=35)
e2 = Entry(master)
e2.configure(bd=4)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
Label(master, text="", background='white').grid(row=3)
build_Button = Button(master, text="Build", command=build_handler, width=25)
classify_Button = Button(master, text="Classify", command=classify_handler, width=25)
browse_Button = Button(master, text="Browse", command=choose_directory)
build_Button.grid(row=4, column=1)
classify_Button.grid(row=6, column=1)
browse_Button.grid(row=1, column=2)
classify_Button.config(state='disabled')
Label(master, text="", background='white').grid(row=5)
mainloop()