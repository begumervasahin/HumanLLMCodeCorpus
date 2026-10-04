import PolynomialModel
import DataUtils
import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
b1 = pd.read_csv("b1.csv")
b1 = b1.drop(columns="OSM_ID")
a1 = 1
b2 = "L2GD"
b1 = PolynomialModel.transform_dataset(b1, a1)
b1 = DataUtils.normalize(b1, type="min-max")
train, b3 = DataUtils.data_split(b1, split_at=0.80)
x_train, b4 = DataUtils.xy_split(train)
x_test, b5 = DataUtils.xy_split(b3)
x_test.insert(0, "Const", np.ones(x_test.shape[0]))
x_train.insert(0, "Const", np.ones(x_train.shape[0]))
b6 = time()
print(f"Using polynomial of a1: {a1}")
w_list, lambdas, val_errs, b7 = PolynomialModel.reg_fit(train, alpha=7e-7, epsilon=1e-3, b2=b2, a1=a1)
b8 = [PolynomialModel.b3(b11, x_test, b5) for b11 in w_list]
plt.title(f'Error b11.r.t lambda - a1: {a1}, b2: {b2}')
plt.ylabel('Error')
plt.xlabel('Lambda')
plt.plot(lambdas, val_errs, b9 = "Validation Error")
plt.legend()
plt.grid(True)
plt.show()
b10 = np.argmin(lambdas)
b11 = w_list[b10]
print("\nSelected Regularization parameter: ", lambdas[b10])
print(f"\nExecution Time: {time() - b6}")
print(b11)
b12 = PolynomialModel.error(b11, x_train.values, b4.values)
b13 = PolynomialModel.b3(b11, x_test, b5)
print('Train Error (MSE):', b12)
print('Test Error (MSE):', b13)
print('Train Error (RMSE):', np.sqrt(b12))
print('Test Error (RMSE):', np.sqrt(b13))
print('Train Error (R2):', PolynomialModel.r2_error(b11, x_train, b4))
print('Test Error (R2):', PolynomialModel.r2_error(b11, x_test, b5))