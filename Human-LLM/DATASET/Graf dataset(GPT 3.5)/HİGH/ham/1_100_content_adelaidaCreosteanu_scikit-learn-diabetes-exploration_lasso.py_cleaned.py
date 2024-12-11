import utility as u
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
def fonk1(dataset):
    x_train, x_test, y_train, b1 = train_test_split(dataset.data, dataset.target, test_size=0.2)
    train_errors, b2 = [], []
    b3 = np.linspace(1e-06,3,1000)
    for _ in b3:
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
def fonk2(dataset):
    b9 = [
        {'alpha': np.logspace(-6,0.5,1000)}
    ]
    b4 = linear_model.Lasso()
    b10 = GridSearchCV(b4, b9, cv=5)
    b10.fit(dataset.data, dataset.target)
    return b10.best_params_['alpha']