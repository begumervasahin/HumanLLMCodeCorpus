import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import metrics
import scipy.optimize
def get_power(dim, order):
    p = (order + 1) ** dim
    base = [int(np.base_repr(i, order + 1)) for i in range(p)]
    base = ["{:02d}".format(int(v)) for v in base]
    for i, v in enumerate(base):
        base[i] = [int(ei) for ei in list(v)]
    return base
def get_data(line):
    return list(map(float, line.strip().split()))
def get_params(file_name):
    with open(file_name, 'r') as f:
        A = get_data(f.readline())
        B = get_data(f.readline())
        Y = [get_data(l) for l in f]
    A, B = np.array(A), np.array(B)
    a1, a2 = A, B
    A, B = np.meshgrid(A, B)
    A, B = A.flatten(), B.flatten()
    Y = np.array(Y).T.flatten()
    return A, B, a1, a2, Y
def polynomial_regression(A, B, Y, order):
    dim = 2
    n = len(Y)
    p = (order + 1) ** dim
    X = np.ones((n, 1))
    e = get_power(dim, order)
    for j in range(1, p):
        ii, iii = e[j]
        X = np.column_stack((X, (A**ii) * (B**iii)))
    model = sm.OLS(Y, X)
    results = model.fit()
    return results, e
def polynomial_function(x, params, e):
    X = [(x[0]**e[i][0]) * (x[1]**e[i][1]) for i in range(len(params))]
    return np.dot(X, params)
def visualize_3d(A, B, Y, F):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(A, B, Y)
    x1 = np.linspace(A.min(), A.max(), 50)
    x2 = np.linspace(B.min(), B.max(), 50)
    x1, x2 = np.meshgrid(x1, x2)
    y = np.array([[F([x1i, x2i]) for x1i in x1] for x2i in x2])
    ax.plot_surface(x1, x2, y, cmap='viridis', alpha=0.5)
    plt.show()
def main():
    print('Reading input file')
    file_name = input('Please input file name:\n')
    print('Initializing inputs')
    A, B, a1, a2, Y = get_params(file_name)
    print('Please input the order for polynomial regression:')
    order = int(input())
    results, e = polynomial_regression(A, B, Y, order)
    params = results.params
    print("\n========")
    print("Parameters:")
    for i, b in enumerate(params):
        ii, iii = e[i]
        print(f"Beta{i} (x{ii}y{iii}) = {b}")
    print(results.summary())
    F = lambda x: polynomial_function(x, params, e)
    visualize_3d(A, B, Y, F)
    Y_p = np.array([F([a, b]) for a, b in zip(A, B)])
    print("R squared score: ", metrics.r2_score(Y, Y_p))
    x_init = np.array([A[0], B[0]])
    bounds = [(A.min(), A.max()), (B.min(), B.max())]
    rslt = scipy.optimize.minimize(F, x_init, method='L-BFGS-B', bounds=bounds)
    x, y = rslt.x
    print("Optima point:")
    print("1st variable = ", x, "; 2nd variable =", y)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(A, B, Y)
    ax.scatter(x, y, F([x, y]), color='r', s=100)
    plt.show()
if __name__ == '__main__':
    main()