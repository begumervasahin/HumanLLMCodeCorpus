import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm, sum_entries
from sklearn.covariance import shrunk_covariance
def ret2prices(ret_series, base_value):
    prices = np.zeros(len(ret_series) + 1)
    prices[0] = base_value
    for i, ret in enumerate(ret_series):
        if np.isnan(ret):
            prices[i + 1] = prices[i]
        else:
            prices[i + 1] = prices[i] * np.exp(ret)
    return prices
def is_pos_def(matrix):
    return np.all(np.linalg.eigvals(matrix) > 0)
def cv_opt(mu, Sigma, e_mu=None, glambda=None, h=0):
    n = len(mu)
    w = Variable(n)
    expected_return = mu.T @ w
    if not is_pos_def(Sigma):
        Sigma = _shrink_covariance_until_pos_def(Sigma)
        if not is_pos_def(Sigma):
            print('Here you got a serious problem', flush=True)
            print(Sigma)
            return _return_nan_arrays(n)
    risk = quad_form(w, Sigma)
    constraints = [sum_entries(w) == 1, w >= h]
    if e_mu is not None:
        constraints.append(expected_return == e_mu)
    if glambda is not None:
        objective = Maximize(expected_return - risk - glambda * norm(w, 1))
    else:
        objective = Maximize(expected_return - risk)
    prob = Problem(objective, constraints)
    prob.solve()
    return _get_results(w, expected_return, risk, n)
def _shrink_covariance_until_pos_def(Sigma):
    for i in np.linspace(0.01, 10000, 1000000):
        shrunk_Sigma = shrunk_covariance(Sigma, shrinkage=i)
        if is_pos_def(shrunk_Sigma):
            return shrunk_Sigma
    return Sigma
def _return_nan_arrays(length):
    return np.full(length, np.nan), np.nan, np.nan
def _get_results(w, ret, risk, length):
    try:
        weights = w.value
        portfolio_return = ret.value
        portfolio_risk = risk.value
    except:
        return _return_nan_arrays(length)
    return weights, portfolio_return, portfolio_risk
