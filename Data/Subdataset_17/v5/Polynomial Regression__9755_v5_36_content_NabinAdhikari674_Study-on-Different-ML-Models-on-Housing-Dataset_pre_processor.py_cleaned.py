import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def print_message(message):
    print(f"\n{message}")
def initialize_data(data):
    inputs = data.iloc[:, :-1]
    targets = data['MEDV']
    print_message("Setting Inputs and Targets DONE.")
    return inputs, targets
def custom_train_test_split(data, percent):
    print_message("Running Train_Test_Split...")
    row_count = data.shape[0]
    test_size = int((percent / 100) * row_count)
    train_size = row_count - test_size
    print_message(f"The size of Training Data is: {train_size}")
    print_message(f"The size of Test Data is: {test_size}")
    print_message(f"Total: {train_size + test_size}")
    train_rows = []
    test_rows = []
    print_message("Randomly Choosing Training Data...")
    while len(train_rows) < train_size:
        row_index = np.random.choice(data.index)
        if row_index not in [row['Sn'] for row in train_rows]:
            row_dict = data.loc[row_index].to_dict()
            train_rows.append(row_dict)
    print_message("Randomly Choosing Test Data...")
    while len(test_rows) < test_size:
        row_index = np.random.choice(data.index)
        if row_index not in [row['Sn'] for row in train_rows] and row_index not in [row['Sn'] for row in test_rows]:
            row_dict = data.loc[row_index].to_dict()
            test_rows.append(row_dict)
    train_df = pd.DataFrame(train_rows)
    test_df = pd.DataFrame(test_rows)
    print_message("The Training and Test Data ARE Split")
    return train_df, test_df
def choose_splitter(inputs, targets):
    choice = input("\nUse Built-IN Splitter (NOT READY!!) ?\nEnter [y/n]: ").strip().lower()
    if choice == 'y':
        print_message("This feature is not implemented yet.")
        return choose_splitter(inputs, targets)
    elif choice == 'n':
        percent = int(input("\nEnter the TEST size (IN PERCENTAGE): "))
        x_train, x_test, y_train, y_test = train_test_split(inputs, targets, test_size=percent/100, random_state=0)
        print_message("The Training & Test Data ARE Split")
    else:
        print_message("Wrong Choice... TRY AGAIN")
        return choose_splitter(inputs, targets)
    return x_train, x_test, y_train, y_test
print_message("\t\t\t\tImporting Packages...")
print_message("Import DONE.")
inputs, targets = initialize_data(data)
Xtrain, Xtest, Ytrain, Ytest = choose_splitter(inputs, targets)
print_message("Exiting pre.py")