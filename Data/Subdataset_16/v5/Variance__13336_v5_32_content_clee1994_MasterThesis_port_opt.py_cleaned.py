import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm
from sklearn.covariance import shrunk_covariance
def fonk1(ret_series, base_value):
    b1 = np.zeros(len(ret_series) + 1)
    b1[0] = base_value
    for i, b6 in enumerate(ret_series):
        if np.isnan(b6):
            b1[i + 1] = b1[i]
        else:
            b1[i + 1] = b1[i] * np.exp(b6)
    return b1
def fonk2(matrix):
    return np.all(np.linalg.eigvals(matrix) > 0)
def fonk3(matrix):
    for i in np.linspace(0.01, 10000, 1000000):
        b2 = shrunk_covariance(matrix, shrinkage=i)
        if fonk2(b2):
            return b2
    raise ValueError("Covariance matrix could not be made positive definite")
def fonk4(mu, b7, b3 = None, glambda=None, h=0):
    b4 = len(mu)
    b5 = Variable(b4)
    b6 = mu.T @ b5
    if not fonk2(b7):
        try:
            b7 = fonk3(b7)
        except ValueError as e:
            print(f"Error: {e}", b8 = True)
            print(b7)
            return np.full(b4, np.nan), np.nan, np.nan
    b9 = quad_form(b5, b7)
    b10 = [sum(b5) == 1, b5 >= h]
    if b3 is not None:
        b10.append(b6 = = b3)
    if glambda is not None:
        b11 = Maximize(b6 - b9 - glambda * norm(b5, 1))
    else:
        b11 = Maximize(b6 - b9)
    b12 = Problem(b11, b10)
    b12.solve()
    try:
        b13 = b5.value
        b14 = b6.value
        b15 = b9.value
    except:
        b13 = np.full(b4, np.nan)
        b14 = np.nan
        b15 = np.nan
    return b13, b14, b15