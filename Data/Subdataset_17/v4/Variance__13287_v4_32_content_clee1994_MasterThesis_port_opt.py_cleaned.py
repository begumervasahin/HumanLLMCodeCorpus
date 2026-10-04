import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm
from sklearn.covariance import shrunk_covariance
def ret2prices(ret_series, base_value):
    prices = np.zeros(len(ret_series) + 1)
    prices[0] = base_value
    for i in range(len(ret_series)):
        if np.isnan(ret_series[i]):
            prices[i + 1] = prices[i]
        else:
            prices[i + 1] = prices[i] * np.exp(ret_series[i])
    return prices
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)
def cv_opt(mu, Sigma, e_mu=None, glambda=None, h=0):
    n = len(mu)
    w = Variable(n)
    ret = mu.T @ w
    if not is_pos_def(Sigma):
        for i in np.linspace(0.01, 10000, 1000000):
            test = shrunk_covariance(Sigma, shrinkage=i)
            if is_pos_def(test):
                Sigma = test
                break
        if not is_pos_def(Sigma):
            print('Error: Covariance matrix is not positive definite', flush=True)
            print(Sigma)
            return np.full(n, np.nan), np.nan, np.nan
    risk = quad_form(w, Sigma)
    constraints = [sum(w) == 1, w >= h]
    if e_mu is not None:
        constraints.append(ret == e_mu)
    if glambda is not None:
        prob = Problem(Maximize(ret - risk - glambda * norm(w, 1)), constraints)
    else:
        prob = Problem(Maximize(ret - risk), constraints)
    prob.solve()
    try:
        rw = w.value
        rr = ret.value
        rri = risk.value
    except:
        rw = np.full(n, np.nan)
        rr = np.nan
        rri = np.nan
    return rw, rr, rri