import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
b1 = pd.read_csv('your_data_file.csv')
b2 = b1.columns
b3 = b1.iloc[:, :-1]
b4 = b1['MEDV']
def fonk1(b1, b11):
    print("\nRunning Custom Train-Test Split...\n")
    b5 = len(b1)
    b6 = int((b11 / 100) * b5)
    b7 = b5 - b6
    print(f"   The size of Training Data is : {b7}")
    print(f"   The size of Test Data is     : {b6}")
    print(f"                          Total : {b7 + b6}")
    b8 = b1.sample(n=b7, random_state=1)
    b9 = b1.drop(b8.b12)
    print("\t\tThe Training and Test Data are Split")
    return b8, b9
def fonk2():
    global b3, b4
    b10 = input("\n\t\tUse Built-IN Splitter (NOT READY!!) ?\nEnter [y/n]:   ").strip().lower()
    if b10 = = 'y':
        b11 = int(input("\n\t\tEnter the TEST size (IN PERCENTAGE): "))
        b8, b9 = fonk1(b1, b11)
        print(f"\nThe Training Data has shape : {b8.shape}")
        print(f"The Test Data has shape     : {b9.shape}")
        b8.to_excel('hello.xlsx', b12 = False)
        b13 = b8.drop(columns=['MEDV'])
        b14 = b9.drop(columns=['MEDV'])
        b15 = b8['MEDV']
        b16 = b9['MEDV']
    elif b10 = = 'n':
        b11 = float(input("\n\t\tEnter the TEST size (IN PERCENTAGE): ")) / 100
        print("\nRandomly Choosing Training and Test Data...\n")
        b13, b14, b15, b16 = train_test_split(b3, b4, b6=b11, random_state=0)
        print("The Training & Test Data are Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        return fonk2()
    return b13, b14, b15, b16
Xtrain, Xtest, Ytrain, b17 = fonk2()
print("\n\tExiting pre.py\n")