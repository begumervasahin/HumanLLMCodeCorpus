import pandas as pd
import numpy as np
print("\n\t\t\t\tImporting Packages...")
print("Import DONE.\n")
inputs = data.iloc[:, :-1]
targets = data['MEDV']
print("Setting Inputs and Targets DONE.\n")
def train_test_split1(data, percent):
    print("\nRunning Train_Test_Split...\n")
    row = data.shape[0]
    test_size = int((percent / 100) * row)
    train_size = row - test_size
    print(f"   The size of Training Data is : {train_size}")
    print(f"   The size of Test Data is     : {test_size}")
    print(f"                          Total : {train_size + test_size}")
    rows_t = []
    rows_s = []
    print("\n\tRandomly Choosing Training Data...\n")
    names = data.columns.tolist()
    while len(rows_t) < train_size:
        x1 = np.random.choice(data.index)
        if x1 not in [row['Sn'] for row in rows_t]:
            row_dict = data.iloc[x1].to_dict()
            rows_t.append(row_dict)
    print("\tRandomly Choosing Test Data...\n")
    while len(rows_s) < test_size:
        x1 = np.random.choice(data.index)
        if (x1 not in [row['Sn'] for row in rows_t]) and (x1 not in [row['Sn'] for row in rows_s]):
            row_dict = data.iloc[x1].to_dict()
            rows_s.append(row_dict)
    train = pd.DataFrame(rows_t, columns=names)
    test = pd.DataFrame(rows_s, columns=names)
    print("\t\tThe Training and Test Data ARE Split")
    return train, test
def choser():
    global inputs, targets
    choose = input("\n\t\tUse Built-IN Splitter(NOT READY!!) ?\nEnter [y/n]:   ").strip().lower()
    if choose == 'y':
        print("\nThis feature is not implemented yet.\n")
        choser()
    elif choose == 'n':
        percent = int(input("\n\t\tEnter the TEST size (IN PERCENTAGE) : "))
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, y_test = train_test_split(inputs, targets, test_size=percent/100, random_state=0)
        print("The Training & Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        return choser()
    return x_train, x_test, y_train, y_test
Xtrain, Xtest, Ytrain, Ytest = choser()
print("\n\tExiting pre.py\n")