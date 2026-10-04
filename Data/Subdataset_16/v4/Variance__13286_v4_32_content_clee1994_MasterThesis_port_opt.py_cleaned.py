import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm
from sklearn.covariance import shrunk_covariance
def fonk1(ret_series, base_value):
    b1 = np.zeros(len(ret_series) + 1)
    b1[0] = base_value
    for i in range(len(ret_series)):
        if np.isnan(ret_series[i]):
            b1[i + 1] = b1[i]
        else:
            b1[i + 1] = b1[i] * np.exp(ret_series[i])
    return b1
def fonk2(x):
    return np.all(np.linalg.eigvals(x) > 0)
def fonk3(mu, b7, b2 = None, glambda=None, h=0):
    b3 = len(mu)
    b4 = Variable(b3)
    b5 = mu.T @ b4
    if not fonk2(b7):
        for i in np.linspace(0.01, 10000, 1000000):
            b6 = shrunk_covariance(b7, shrinkage=i)
            if fonk2(b6):
                b7 = b6
                break
        if not fonk2(b7):
            print('Error: Covariance matrix is not positive definite', b8 = True)
            print(b7)
            return np.full(b3, np.nan), np.nan, np.nan
    b9 = quad_form(b4, b7)
    b10 = [sum(b4) == 1, b4 >= h]
    if b2 is not None:
        b10.append(b5 = = b2)
    if glambda is not None:
        b11 = Problem(Maximize(b5 - b9 - glambda * norm(b4, 1)), b10)
    else:
        b11 = Problem(Maximize(b5 - b9), b10)
    b11.solve()
    try:
        b12 = b4.value
        b13 = b5.value
        b14 = b9.value
    except:
        b12 = np.full(b3, np.nan)
        b13 = np.nan
        b14 = np.nan
    return b12, b13, b14