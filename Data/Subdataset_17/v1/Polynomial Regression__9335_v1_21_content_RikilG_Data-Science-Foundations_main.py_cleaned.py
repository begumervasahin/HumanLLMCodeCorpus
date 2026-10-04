import PolynomialModel
import DataUtils
import pandas as pd
import numpy as np
from time import time
import matplotlib.pyplot as plt
dataset = pd.read_csv("dataset.csv")
dataset = dataset.drop(columns="OSM_ID")
degree = 1
method = "L2GD"
dataset = PolynomialModel.transform_dataset(dataset, degree)
dataset = DataUtils.normalize(dataset, type="min-max")
train, test = DataUtils.data_split(dataset, split_at=0.80)
x_train, y_train = DataUtils.xy_split(train)
x_test, y_test = DataUtils.xy_split(test)
x_test.insert(0, "Const", np.ones(x_test.shape[0]))
x_train.insert(0, "Const", np.ones(x_train.shape[0]))
st_time = time()
print(f"Using polynomial of degree: {degree}")
w_list, lamdas, val_errs, train_errs = PolynomialModel.reg_fit(train, alpha=7e-7, epsilion=1e-3, method=method, degree=degree)
test_errs = [PolynomialModel.test(w, x_test, y_test) for w in w_list]
plt.title(f'Error w.r.t lambda - degree: {degree}, method: {method}')
plt.ylabel('Error')
plt.xlabel('Lambda')
plt.plot(lamdas, val_errs, label="validation error")
plt.legend()
plt.grid(True)
plt.show()
min_index = np.argmin(val_errs)
w = w_list[min_index]
print("\nSelected Reg param: ", lamdas[min_index])
print(f"\nExecution Time : {time() - st_time}")
print(w)
print('Train Error (MSE):\t', PolynomialModel.error(w, x_train.values, y_train.values))
print('Test Error (MSE):\t', PolynomialModel.test(w, x_test, y_test))
print('Train Error (RMSE):\t', PolynomialModel.error(w, x_train.values, y_train.values) ** 0.5)
print('Test Error (RMSE):\t', PolynomialModel.test(w, x_test, y_test) ** 0.5)
print('Train Error (R2):\t', PolynomialModel.r2_error(w, x_train, y_train))
print('Test Error (R2):\t', PolynomialModel.r2_error(w, x_test, y_test))