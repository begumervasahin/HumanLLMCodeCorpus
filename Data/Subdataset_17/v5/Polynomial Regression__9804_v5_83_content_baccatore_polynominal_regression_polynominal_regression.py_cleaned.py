import numpy as np
from statsmodels import api as sm
import scipy.optimize
from sklearn import metrics
from matplotlib import pyplot as plt
def get_power(dim, order):
    p = (order + 1) ** dim
    base = [int(np.base_repr(i, order + 1)) for i in range(p)]
    base = ["{:02d}".format(int(v)) for v in base]
    for i, v in enumerate(base):
        base[i] = [int(ei) for ei in list(v)]
    return base
def get_params(file_name):
    with open(file_name, 'r') as f:
        Y = []
        A = lm.get_data(f.readline())
        B = lm.get_data(f.readline())
        for line in f:
            Y.append(lm.get_data(line))
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
    X = np.ones(n)
    exponents = get_power(dim, order)
    for j in range(1, p):
        ii, iii = exponents[j]
        X = np.column_stack((X, (A**ii) * (B**iii)))
    model = sm.OLS(Y, X)
    results = model.fit()
    return results, exponents
def predict(F, a1, a2):
    return np.array([[F([x1i, x2i]) for x1i in a1] for x2i in a2]).flatten()
def plot_surface(ax, A, B, Y, F):
    x1 = np.linspace(A.min(), A.max(), 100)
    x2 = np.linspace(B.min(), B.max(), 100)
    x1, x2 = np.meshgrid(x1, x2)
    y = np.array([[F([x1i, x2i]) for x1i in x1] for x2i in x2])
    ax.plot_surface(x1, x2, y, cmap='viridis')
    ax.scatter(A, B, Y)
def main():
    print('Reading input file')
    file_name = input('Please input file name: ')
    print(file_name)
    print('Initializing inputs')
    A, B, a1, a2, Y = get_params(file_name)
    print('Please input the order for polynomial regression:')
    order = int(input())
    results, exponents = polynomial_regression(A, B, Y, order)
    params = results.params
    print("\n========")
    print("Parameters: ")
    for i, b in enumerate(params):
        ii, iii = exponents[i]
        print(f"Beta{i} (x{ii}y{iii}) = {b}")
    print(results.summary())
    def F(x):
        X = [(x[0]**exponents[i][0]) * (x[1]**exponents[i][1]) for i in range(len(params))]
        X = np.array(X)
        return np.dot(X, params)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plot_surface(ax, A, B, Y, F)
    Y_pred = predict(F, a1, a2)
    print("R squared score: ", metrics.r2_score(Y, Y_pred))
    x_init = np.array([A[1], B[1]])
    bounds = np.array([[A.min(), A.max()], [B.min(), B.max()]])
    result = scipy.optimize.minimize(F, x_init, method='L-BFGS-B', bounds=bounds)
    x_opt, y_opt = result.x
    print("Optima point:")
    print(f"1st variable = {x_opt}; 2nd variable = {y_opt}")
    ax.scatter(x_opt, y_opt, F([x_opt, y_opt]), color='r', marker='x')
    plt.show()
if __name__ == '__main__':
    main()