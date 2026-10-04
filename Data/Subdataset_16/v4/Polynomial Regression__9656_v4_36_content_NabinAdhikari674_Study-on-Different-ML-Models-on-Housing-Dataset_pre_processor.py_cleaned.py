import pandas as pd
import numpy as np
print("\n\t\t\t\tImporting Packages...")
print("Import DONE.\n")
b1 = data.iloc[:, :-1]
b2 = data['MEDV']
print("Setting Inputs and Targets DONE.\n")
def fonk1(data, b14):
    print("\nRunning Train_Test_Split...\n")
    b3 = data.shape[0]
    b4 = int((b14 / 100) * b3)
    b5 = b3 - b4
    print(f"   The size of Training Data is : {b5}")
    print(f"   The size of Test Data is     : {b4}")
    print(f"                          Total : {b5 + b4}")
    b6 = []
    b7 = []
    print("\n\tRandomly Choosing Training Data...\n")
    b8 = data.columns.tolist()
    while len(b6) < b5:
        b9 = np.random.choice(data.index)
        if b9 not in [b3['Sn'] for b3 in b6]:
            b10 = data.iloc[b9].to_dict()
            b6.append(b10)
    print("\tRandomly Choosing Test Data...\n")
    while len(b7) < b4:
        b9 = np.random.choice(data.index)
        if (b9 not in [b3['Sn'] for b3 in b6]) and (b9 not in [b3['Sn'] for b3 in b7]):
            b10 = data.iloc[b9].to_dict()
            b7.append(b10)
    b11 = pd.DataFrame(b6, columns=b8)
    b12 = pd.DataFrame(b7, columns=b8)
    print("\t\tThe Training and Test Data ARE Split")
    return b11, b12
def fonk2():
    global b1, b2
    b13 = input("\n\t\tUse Built-IN Splitter(NOT READY!!) ?\nEnter [y/n]:   ").strip().lower()
    if b13 = = 'y':
        print("\nThis feature is not implemented yet.\n")
        fonk2()
    elif b13 = = 'n':
        b14 = int(input("\n\t\tEnter the TEST size (IN PERCENTAGE) : "))
        from sklearn.model_selection import train_test_split
        x_train, x_test, y_train, b15 = train_test_split(b1, b2, b4=b14/100, random_state=0)
        print("The Training & Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        return fonk2()
    return x_train, x_test, y_train, b15
Xtrain, Xtest, Ytrain, b16 = fonk2()
print("\n\tExiting pre.py\n")