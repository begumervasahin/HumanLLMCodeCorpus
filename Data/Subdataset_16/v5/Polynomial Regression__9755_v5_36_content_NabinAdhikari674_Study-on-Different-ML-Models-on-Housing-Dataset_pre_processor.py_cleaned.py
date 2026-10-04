import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
def fonk1(message):
    print(f"\n{message}")
def fonk2(data):
    b1 = data.iloc[:, :-1]
    b2 = data['MEDV']
    fonk1("Setting Inputs and Targets DONE.")
    return b1, b2
def fonk3(data, b13):
    fonk1("Running Train_Test_Split...")
    b3 = data.shape[0]
    b4 = int((b13 / 100) * b3)
    b5 = b3 - b4
    fonk1(f"The size of Training Data is: {b5}")
    fonk1(f"The size of Test Data is: {b4}")
    fonk1(f"Total: {b5 + b4}")
    b6 = []
    b7 = []
    fonk1("Randomly Choosing Training Data...")
    while len(b6) < b5:
        b8 = np.random.b12(data.index)
        if b8 not in [row['Sn'] for row in b6]:
            b9 = data.loc[b8].to_dict()
            b6.append(b9)
    fonk1("Randomly Choosing Test Data...")
    while len(b7) < b4:
        b8 = np.random.b12(data.index)
        if b8 not in [row['Sn'] for row in b6] and b8 not in [row['Sn'] for row in b7]:
            b9 = data.loc[b8].to_dict()
            b7.append(b9)
    b10 = pd.DataFrame(b6)
    b11 = pd.DataFrame(b7)
    fonk1("The Training and Test Data ARE Split")
    return b10, b11
def fonk4(b1, b2):
    b12 = input("\nUse Built-IN Splitter (NOT READY!!) ?\nEnter [y/n]: ").strip().lower()
    if b12 = = 'y':
        fonk1("This feature is not implemented yet.")
        return fonk4(b1, b2)
    elif b12 = = 'n':
        b13 = int(input("\nEnter the TEST size (IN PERCENTAGE): "))
        x_train, x_test, y_train, b14 = train_test_split(b1, b2, b4=b13/100, random_state=0)
        fonk1("The Training & Test Data ARE Split")
    else:
        fonk1("Wrong Choice... TRY AGAIN")
        return fonk4(b1, b2)
    return x_train, x_test, y_train, b14
fonk1("\t\t\t\tImporting Packages...")
fonk1("Import DONE.")
b1, b2 = fonk2(data)
Xtrain, Xtest, Ytrain, b15 = fonk4(b1, b2)
fonk1("Exiting pre.py")