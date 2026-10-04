import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv('your_data_file.csv')
names = data.columns
inputs = data.iloc[:, :-1]
targets = data['MEDV']
def train_test_split_custom(data, percent):
    print("\nRunning Train_Test_Split...\n")
    row_count = len(data)
    test_size = int((percent / 100) * row_count)
    train_size = row_count - test_size
    print(f"   The size of Training Data is : {train_size}")
    print(f"   The size of Test Data is     : {test_size}")
    print(f"                          Total : {train_size + test_size}")
    train_data = data.sample(n=train_size, random_state=1)
    test_data = data.drop(train_data.index)
    print("\t\tThe Training and Test Data ARE Split")
    return train_data, test_data
def choose_split_method():
    global inputs, targets
    choice = input("\n\t\tUse Built-IN Splitter (NOT READY!!) ?\nEnter [y/n]:   ").strip().lower()
    if choice == 'y':
        percent = int(input("\n\t\tEnter the TEST size (IN PERCENTAGE) : "))
        train_data, test_data = train_test_split_custom(data, percent)
        print(f"\nThe Training Data has shape : {train_data.shape}")
        print(f"The Test Data has shape     : {test_data.shape}")
        train_data.to_excel('hello.xlsx', index=False)
        x_train = train_data.drop(columns=['MEDV'])
        x_test = test_data.drop(columns=['MEDV'])
        y_train = train_data['MEDV']
        y_test = test_data['MEDV']
    elif choice == 'n':
        percent = float(input("\n\t\tEnter the TEST size (IN PERCENTAGE) : ")) / 100
        print("\nRandomly Choosing Training and Test Data...\n")
        x_train, x_test, y_train, y_test = train_test_split(inputs, targets, test_size=percent, random_state=0)
        print("The Training & Test Data ARE Split")
    else:
        print("Wrong Choice...TRY AGAIN\n")
        return choose_split_method()
    return x_train, x_test, y_train, y_test
Xtrain, Xtest, Ytrain, Ytest = choose_split_method()
print("\n\tExiting pre.py\n")