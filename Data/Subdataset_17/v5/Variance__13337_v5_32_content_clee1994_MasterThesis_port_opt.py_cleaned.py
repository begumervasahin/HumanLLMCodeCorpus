import numpy as np
from cvxpy import quad_form, Variable, Problem, Maximize, norm
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
def make_pos_def(matrix):
    for i in np.linspace(0.01, 10000, 1000000):
        test_matrix = shrunk_covariance(matrix, shrinkage=i)
        if is_pos_def(test_matrix):
            return test_matrix
    raise ValueError("Covariance matrix could not be made positive definite")
def cv_opt(mu, Sigma, e_mu=None, glambda=None, h=0):
    n = len(mu)
    w = Variable(n)
    ret = mu.T @ w
    if not is_pos_def(Sigma):
        try:
            Sigma = make_pos_def(Sigma)
        except ValueError as e:
            print(f"Error: {e}", flush=True)
            print(Sigma)
            return np.full(n, np.nan), np.nan, np.nan
    risk = quad_form(w, Sigma)
    constraints = [sum(w) == 1, w >= h]
    if e_mu is not None:
        constraints.append(ret == e_mu)
    if glambda is not None:
        objective = Maximize(ret - risk - glambda * norm(w, 1))
    else:
        objective = Maximize(ret - risk)
    prob = Problem(objective, constraints)
    prob.solve()
    try:
        optimized_weights = w.value
        expected_return = ret.value
        portfolio_risk = risk.value
    except:
        optimized_weights = np.full(n, np.nan)
        expected_return = np.nan
        portfolio_risk = np.nan
    return optimized_weights, expected_return, portfolio_risk