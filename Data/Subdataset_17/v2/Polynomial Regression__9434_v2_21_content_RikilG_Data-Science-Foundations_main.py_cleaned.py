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
start_time = time()
print(f"Using polynomial of degree: {degree}")
w_list, lambdas, val_errs, train_errs = PolynomialModel.reg_fit(train, alpha=7e-7, epsilion=1e-3, method=method, degree=degree)
test_errs = [PolynomialModel.test(w, x_test, y_test) for w in w_list]
plt.title(f'Error w.r.t lambda - degree: {degree}, method: {method}')
plt.ylabel('Error')
plt.xlabel('Lambda')
plt.plot(lambdas, val_errs, label="Validation Error")
plt.legend()
plt.grid(True)
plt.show()
min_index = np.argmin(val_errs)
best_lambda = lambdas[min_index]
best_weights = w_list[min_index]
print(f"\nSelected Regularization Parameter: {best_lambda}")
print(f"\nExecution Time: {time() - start_time} seconds")
print("Weights:\n", best_weights)
train_mse = PolynomialModel.error(best_weights, x_train.values, y_train.values)
test_mse = PolynomialModel.test(best_weights, x_test, y_test)
print('Train Error (MSE):\t', train_mse)
print('Test Error (MSE):\t', test_mse)
print('Train Error (RMSE):\t', np.sqrt(train_mse))
print('Test Error (RMSE):\t', np.sqrt(test_mse))
print('Train Error (R2):\t', PolynomialModel.r2_error(best_weights, x_train, y_train))
print('Test Error (R2):\t', PolynomialModel.r2_error(best_weights, x_test, y_test))