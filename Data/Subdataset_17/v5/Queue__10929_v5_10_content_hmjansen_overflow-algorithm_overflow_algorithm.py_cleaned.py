
import numpy as np
import scipy.linalg as linalg
def solve_linearized_equation(n, alpha, mu, P, Q, A_set, B_set):
    alpha, mu, P, Q = map(np.asarray, (alpha, mu, P, Q))
    P_A = np.zeros((n, n))
    Q_B = np.zeros((n, n))
    for i in range(n):
        if i in A_set:
            P_A[i, :] = P[i, :]
        if i in B_set:
            Q_B[i, :] = Q[i, :]
    P_A_bar = P - P_A
    I = np.eye(n)
    X = np.transpose(I - P_A - Q_B)
    z = np.transpose(alpha + mu @ (P_A_bar - Q_B))
    y = linalg.solve(X, z)
    return y.T
def solve_overflow_traffic_equation(alpha, mu, P, Q, count=False):
    n = len(alpha)
    alpha, mu, P, Q = map(np.asarray, (alpha, mu, P, Q))
    solve_count = 0
    N_set = set(range(n))
    B_set = set()
    previous_B_set = None
    while B_set != previous_B_set:
        previous_B_set = B_set.copy()
        A_set = set()
        previous_A_set = None
        while A_set != previous_A_set:
            previous_A_set = A_set.copy()
            labda = solve_linearized_equation(n, alpha, mu, P, Q, A_set, B_set)
            A_set = {i for i in range(n) if labda[i] < mu[i]}
            solve_count += 1
        B_set = N_set - A_set
    zeros = np.zeros(n)
    labda_check = alpha + np.minimum(labda, mu) @ P + np.maximum(labda - mu, zeros) @ Q
    if not np.allclose(labda, labda_check):
        print("\nWarning: solution may be incorrect\n")
    if count:
        max_count = int(1 + (0.5 * n * (n + 1)))
        return labda, solve_count, max_count
    else:
        return labda
