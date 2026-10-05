import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import load_diabetes
import utility as u
def fonk1(b11):
    x_train, x_test, y_train, b1 = train_test_split(b11.data, b11.target, test_size=0.2, random_state=42)
    train_errors, b2 = [], []
    b3 = np.linspace(1e-06, 3, 1000)
    for alpha in b3:
        b6, b4 = fonk2(x_train, y_train, x_test, b1, alpha)
        train_errors.append(b6)
        b2.append(b4)
    fonk3(b3, train_errors, b2)
def fonk2(x_train, y_train, x_test, b1, alpha):
    b5 = linear_model.Lasso(alpha=alpha)
    b5.fit(x_train, y_train)
    b6 = u.rmse(y_train, b5.predict(x_train))
    b4 = u.rmse(b1, b5.predict(x_test))
    return b6, b4
def fonk3(b3, train_errors, b2):
    plt.plot(b3, train_errors, 'r-', b7 = 2, label='Training')
    plt.plot(b3, b2, 'b-', b7 = 3, label='Validation')
    plt.xlabel('Alpha')
    plt.ylabel('RMSE')
    plt.legend(b8 = 'lower right')
    plt.show()
def fonk4(b11):
    b9 = [{'alpha': np.logspace(-6, 0.5, 1000)}]
    b5 = linear_model.Lasso()
    b10 = GridSearchCV(b5, b9, cv=5)
    b10.fit(b11.data, b11.target)
    return b10.best_params_['alpha']
b11 = load_diabetes()
fonk1(b11)
b12 = fonk4(b11)
print("Optimal Alpha:", b12)