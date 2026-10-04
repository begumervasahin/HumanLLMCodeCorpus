import PolynomialModel
import DataUtils
import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
def fonk1():
    b1 = fonk2("b1.csv")
    a1 = 1
    b2 = "L2GD"
    b1 = fonk3(b1, a1)
    x_train, b5, x_test, b3 = fonk4(b1)
    fonk5(x_train, b5, x_test, b3, a1, b2)
def fonk2(file_path):
    b1 = pd.read_csv(file_path)
    b1 = b1.drop(columns="OSM_ID")
    return b1
def fonk3(b1, a1):
    b1 = PolynomialModel.transform_dataset(b1, a1)
    b1 = DataUtils.normalize(b1, type="min-max")
    return b1
def fonk4(b1):
    train, b4 = DataUtils.data_split(b1, split_at=0.80)
    x_train, b5 = DataUtils.xy_split(train)
    x_test, b3 = DataUtils.xy_split(b4)
    x_train.insert(0, "Const", np.ones(x_train.shape[0]))
    x_test.insert(0, "Const", np.ones(x_test.shape[0]))
    return x_train, b5, x_test, b3
def fonk5(x_train, b5, x_test, b3, a1, b2):
    b6 = time()
    print(f"Using polynomial of a1: {a1}")
    w_list, lambdas, val_errs, b7 = PolynomialModel.reg_fit(
        pd.concat([x_train, b5], b8 = 1), alpha=7e-7, epsilion=1e-3, b2=b2, a1=a1
    )
    b9 = [PolynomialModel.b4(w, x_test, b3) for w in w_list]
    fonk6(lambdas, val_errs, a1, b2)
    b13, b10 = fonk7(lambdas, val_errs, w_list)
    print(f"\nSelected Regularization Parameter: {b13}")
    print(f"\nExecution Time: {time() - b6} seconds")
    print("Weights:\n", b10)
    fonk8(b10, x_train, b5, x_test, b3)
def fonk6(lambdas, val_errs, a1, b2):
    plt.title(f'Error w.r.t lambda - a1: {a1}, b2: {b2}')
    plt.ylabel('Error')
    plt.xlabel('Lambda')
    plt.plot(lambdas, val_errs, b11 = "Validation Error")
    plt.legend()
    plt.grid(True)
    plt.show()
def fonk7(lambdas, val_errs, w_list):
    b12 = np.argmin(val_errs)
    b13 = lambdas[b12]
    b10 = w_list[b12]
    return b13, b10
def fonk8(b10, x_train, b5, x_test, b3):
    b14 = PolynomialModel.error(b10, x_train.values, b5.values)
    b15 = PolynomialModel.b4(b10, x_test, b3)
    print('Train Error (MSE):\t', b14)
    print('Test Error (MSE):\t', b15)
    print('Train Error (RMSE):\t', np.sqrt(b14))
    print('Test Error (RMSE):\t', np.sqrt(b15))
    print('Train Error (R2):\t', PolynomialModel.r2_error(b10, x_train, b5))
    print('Test Error (R2):\t', PolynomialModel.r2_error(b10, x_test, b3))
if b16 = = "__main__":
    fonk1()