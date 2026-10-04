import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm, sum_entries
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
        Sigma = _shrink_covariance_until_pos_def(Sigma)
        if not is_pos_def(Sigma):
            print('Here you got a serious problem', flush=True)
            print(Sigma)
            return _return_nan_arrays(len(mu))
    risk = quad_form(w, Sigma)
    constraints = [sum_entries(w) == 1, w >= h]
    if e_mu is not None:
        constraints.append(ret == e_mu)
    if glambda is not None:
        objective = Maximize(ret - risk - glambda * norm(w, 1))
    else:
        objective = Maximize(ret - risk)
    prob = Problem(objective, constraints)
    prob.solve()
    return _get_results(w, ret, risk, len(mu))
def _shrink_covariance_until_pos_def(Sigma):
    for i in np.linspace(0.01, 10000, 1000000):
        shrunk_Sigma = shrunk_covariance(Sigma, shrinkage=i)
        if is_pos_def(shrunk_Sigma):
            return shrunk_Sigma
    return Sigma
def _return_nan_arrays(length):
    rw = np.empty(length)
    rw[:] = np.nan
    rr = np.nan
    rri = np.nan
    return rw, rr, rri
def _get_results(w, ret, risk, length):
    try:
        rw = w.value
        rr = ret.value
        rri = risk.value
    except:
        return _return_nan_arrays(length)
    return rw, rr, rri
