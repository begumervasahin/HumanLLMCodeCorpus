import utility as u
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_diabetes
def fonk1(b11):
    x_train, x_test, y_train, b1 = train_test_split(b11.data, b11.target, test_size=0.2, random_state=42)
    train_errors, b2 = [], []
    b3 = np.linspace(1e-06, 3, 1000)
    for m in b3:
        b4 = linear_model.Lasso(alpha=m)
        b4.fit(x_train, y_train)
        b5 = u.rmse(y_train, b4.predict(x_train))
        b6 = u.rmse(b1, b4.predict(x_test))
        train_errors.append(b5)
        b2.append(b6)
    plt.plot(b3, train_errors, 'r-', b7 = 2, label='training')
    plt.plot(b3, b2, 'b-', b7 = 3, label='validation')
    plt.xlabel('alpha')
    plt.ylabel('RMSE')
    plt.legend(b8 = 'lower right')
    plt.show()
def fonk2(b11):
    b9 = [{'alpha': np.logspace(-6, 0.5, 1000)}]
    b4 = linear_model.Lasso()
    b10 = GridSearchCV(b4, b9, cv=5)
    b10.fit(b11.data, b11.target)
    return b10.best_params_['alpha']
b11 = load_diabetes()
fonk1(b11)
b12 = fonk2(b11)
print("Optimal Alpha:", b12)