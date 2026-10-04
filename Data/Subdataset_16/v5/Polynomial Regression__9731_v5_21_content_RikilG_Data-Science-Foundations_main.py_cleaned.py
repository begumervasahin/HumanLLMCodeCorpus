import PolynomialModel
import DataUtils
import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
def fonk1(b13, b14, a1):
    b1 = pd.read_csv(b13)
    b1 = b1.drop(columns=b14)
    b1 = PolynomialModel.transform_dataset(b1, a1)
    b1 = DataUtils.normalize(b1, type="min-max")
    return b1
def fonk2(b1, a4):
    train, b2 = DataUtils.data_split(b1, split_at=a4)
    x_train, b3 = DataUtils.xy_split(train)
    b16, b4 = DataUtils.xy_split(b2)
    return x_train, b3, b16, b4
def fonk3(x_train, b16):
    x_train.insert(0, "Const", np.ones(x_train.shape[0]))
    b16.insert(0, "Const", np.ones(b16.shape[0]))
    return x_train, b16
def fonk4(train, b16, b4, b15, a1, a2, a3):
    w_list, lambdas, val_errs, b5 = PolynomialModel.reg_fit(train, a2=a2, a3=a3, b15=b15, a1=a1)
    b6 = [PolynomialModel.b2(w, b16, b4) for w in w_list]
    plt.title(f'Error w.r.t lambda - a1: {a1}, b15: {b15}')
    plt.ylabel('Error')
    plt.xlabel('Lambda')
    plt.plot(lambdas, val_errs, b7 = "Validation Error")
    plt.legend()
    plt.grid(True)
    plt.show()
    return w_list, lambdas, b6
def fonk5(w_list, lambdas):
    b8 = np.argmin(lambdas)
    b9 = lambdas[b8]
    b10 = w_list[b8]
    return b9, b10
def fonk6(w, x_train, b3, b16, b4):
    b11 = PolynomialModel.error(w, x_train.values, b3.values)
    b12 = PolynomialModel.b2(w, b16, b4)
    print('Train Error (MSE):', b11)
    print('Test Error (MSE):', b12)
    print('Train Error (RMSE):', np.sqrt(b11))
    print('Test Error (RMSE):', np.sqrt(b12))
    print('Train Error (R2):', PolynomialModel.r2_error(w, x_train, b3))
    print('Test Error (R2):', PolynomialModel.r2_error(w, b16, b4))
def fonk7():
    b13 = "b1.csv"
    b14 = "OSM_ID"
    a1 = 1
    b15 = "L2GD"
    a2 = 7e-7
    a3 = 1e-3
    a4 = 0.80
    b1 = fonk1(b13, b14, a1)
    x_train, b3, b16, b4 = fonk2(b1, a4)
    x_train, b16 = fonk3(x_train, b16)
    print(f"Using polynomial of a1: {a1}")
    b17 = time()
    w_list, lambdas, b6 = fonk4((x_train, b3), b16, b4, b15, a1, a2, a3)
    b9, b10 = fonk5(w_list, lambdas)
    print("\nSelected Regularization parameter: ", b9)
    print(f"\nExecution Time: {time() - b17}")
    print(b10)
    fonk6(b10, x_train, b3, b16, b4)
if b18 = = "__main__":
    fonk7()