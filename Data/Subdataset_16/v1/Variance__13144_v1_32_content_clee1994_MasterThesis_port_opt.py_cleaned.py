import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm, sum_entries
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
def fonk3(mu, b6, b2 = None, glambda=None, h=0):
    b3 = len(mu)
    b4 = Variable(b3)
    b5 = mu.T @ b4
    if not fonk2(b6):
        b6 = fonk4(b6)
        if not fonk2(b6):
            print('Here you got a serious problem', b7 = True)
            print(b6)
            return fonk5(len(mu))
    b8 = quad_form(b4, b6)
    b9 = [sum_entries(b4) == 1, b4 >= h]
    if b2 is not None:
        b9.append(b5 = = b2)
    if glambda is not None:
        b10 = Maximize(b5 - b8 - glambda * norm(b4, 1))
    else:
        b10 = Maximize(b5 - b8)
    b11 = Problem(b10, b9)
    b11.solve()
    return fonk6(b4, b5, b8, len(mu))
def fonk4(b6):
    for i in np.linspace(0.01, 10000, 1000000):
        b12 = shrunk_covariance(b6, shrinkage=i)
        if fonk2(b12):
            return b12
    return b6
def fonk5(length):
    b13 = np.empty(length)
    b13[:] = np.nan
    b14 = np.nan
    b15 = np.nan
    return b13, b14, b15
def fonk6(b4, b5, b8, length):
    try:
        b13 = b4.value
        b14 = b5.value
        b15 = b8.value
    except:
        return fonk5(length)
    return b13, b14, b15
