import pandas as pd
import os
import re
import PreProcessing as pp
import Classifier as cl
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
class NaiveBayesClassifierApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Naive Bayes Classifier")
        self.master.configure(background='white')
        self.master.geometry("400x300")
        self.path_to_train = ""
        self.path_to_test = ""
        self.path_to_structure = ""
        self.num_of_intervals = 0
        self.setup_gui()
    def setup_gui(self):
        Label(self.master, text="", background='white').grid(row=0)
        Label(self.master, text="Directory Path:", background='white').grid(row=1)
        Label(self.master, text="Discretization Bins:", background='white').grid(row=2)
        self.dir_entry = Entry(self.master, bd=4, width=35)
        self.dir_entry.grid(row=1, column=1)
        self.bins_entry = Entry(self.master, bd=4)
        self.bins_entry.grid(row=2, column=1)
        Label(self.master, text="", background='white').grid(row=3)
        self.build_button = Button(self.master, text="Build", command=self.build_handler, width=25, state=DISABLED)
        self.build_button.grid(row=4, column=1)
        Label(self.master, text="", background='white').grid(row=5)
        self.classify_button = Button(self.master, text="Classify", command=self.classify_handler, width=25, state=DISABLED)
        self.classify_button.grid(row=6, column=1)
        browse_button = Button(self.master, text="Browse", command=self.choose_directory)
        browse_button.grid(row=1, column=2)
    def choose_directory(self):
        dir_path = askdirectory()
        self.dir_entry.insert(10, dir_path)
        self.path_to_train = os.path.join(dir_path, "train.csv")
        self.path_to_test = os.path.join(dir_path, "test.csv")
        self.path_to_structure = os.path.join(dir_path, "Structure.txt")
        missing_files = self.check_missing_files()
        if missing_files:
            self.build_button.config(state=DISABLED)
            showinfo("Naive Bayes Classifier", "The following files are missing:\n" + "\n".join(missing_files))
        else:
            self.build_button.config(state=NORMAL)
    def check_missing_files(self):
        required_files = [self.path_to_train, self.path_to_test, self.path_to_structure]
        missing_files = [os.path.basename(file_path) for file_path in required_files if not os.path.exists(file_path)]
        return missing_files
    def build_handler(self):
        try:
            num_bins = int(self.bins_entry.get())
            if num_bins < 2:
                showinfo("Naive Bayes Classifier", "Discretization bins must be at least 2")
                return
        except ValueError:
            showinfo("Naive Bayes Classifier", "Discretization bins must be an integer")
            return
        if os.stat(self.path_to_structure).st_size == 0:
            showinfo("Naive Bayes Classifier", "The file Structure.txt is empty. Please load valid files")
            return
        try:
            df_train = pd.read_csv(self.path_to_train)
            total_num_records_train = df_train.shape[0]
            if num_bins > total_num_records_train:
                showinfo("Naive Bayes Classifier", "Discretization bins must not be greater than the number of train set records")
                return
            with open(self.path_to_structure, "r") as structure_file:
                df_train_final = pp.preProcess(structure_file, df_train, num_bins)
                attribute_values_dict = pp.set_attribute_values_dict(structure_file)
                cl.prepareModel(df_train_final, self.path_to_structure, num_bins, attribute_values_dict)
            self.classify_button.config(state=NORMAL)
            showinfo("Naive Bayes Classifier", "Building classifier using train-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
    def classify_handler(self):
        try:
            df_test = pd.read_csv(self.path_to_test)
            with open(self.path_to_structure, "r") as structure_file:
                df_test_final = pp.preProcess_test(structure_file, df_test)
                df_test_final.drop(columns=['class'], inplace=True)
                cl.classify(df_test_final, df_train_final, self.dir_entry.get())
                self.classify_button.config(state=DISABLED)
                showinfo("Naive Bayes Classifier", "Classification process of test-set is done!")
        except Exception as e:
            showinfo("Naive Bayes Classifier", f"Error: {str(e)}")
if __name__ == "__main__":
    root = Tk()
    app = NaiveBayesClassifierApp(root)
    root.mainloop()