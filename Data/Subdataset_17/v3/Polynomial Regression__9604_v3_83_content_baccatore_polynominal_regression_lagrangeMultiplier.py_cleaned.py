import numpy as np
import itertools
from statistics import mean
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def get_data(seq):
    return [float(v) for v in seq.split(',')]
def get_power(dim, order):
    num_combinations = (order + 1) ** dim
    base_combinations = [int(np.base_repr(i, base=3)) for i in range(num_combinations)]
    formatted_combinations = ["{:02d}".format(int(v)) for v in base_combinations]
    for i, v in enumerate(formatted_combinations):
        ii, iii = list(v)
        formatted_combinations[i] = (int(ii), int(iii))
    return formatted_combinations[1:]
def coef_of_determination(y, f):
    f_bar = mean(f)
    SSR = sum([(fi - f_bar)**2 for fi in f])
    SST = sum([(yi - y_bar)**2 for yi in y])
    SSE = sum([(yi - fi)**2 for yi, fi in zip(f, y)])
    r2 = SSR / SST
    print((SSR + SSE) / SST)
    return r2
def read_input_data(filename):
    with open(filename, 'r') as f:
        Y = []
        A = get_data(f.readline())
        B = get_data(f.readline())
        for line in f:
            Y.append(get_data(line))
    Y = np.array(Y).T.flatten()
    return A, B, Y
def construct_equations(A, B, Y, dim, order):
    p = (order + 1) ** dim - 1
    n = len(A) * len(B)
    S = np.zeros([p, p])
    a = np.zeros([p])
    x = np.zeros([n, p])
    y = np.zeros([n])
    params = [(a, b) for a, b in itertools.product(A, B)]
    params = np.array(params)
    powers = get_power(dim, order)
    for i in range(n):
        for j in range(p):
            ii, iii = powers[j]
            x[i][j] = (params[i][0] ** ii) * (params[i][1] ** iii)
    y = np.array(Y)
    return x, y, S, a, p
def compute_matrices(x, y, S, p):
    x_bar = [mean(x[:, j]) for j in range(p)]
    y_bar = mean(y)
    for j, k in itertools.product(range(p), repeat=2):
        S[j][k] = sum([(x[i][j] - x_bar[j]) * (x[i][k] - x_bar[k]) for i in range(len(y))])
    M = np.zeros([p])
    for j in range(p):
        M[j] = sum([(x[i][j] - x_bar[j]) * (y[i] - y_bar) for i in range(len(y))])
    return S, M, x_bar, y_bar
def compute_coefficients(S, M, x_bar, y_bar):
    a = np.dot(np.linalg.inv(S), M)
    a0 = y_bar - np.dot(a, x_bar)
    return a, a0
def generate_polynomial_function(a, a0, powers):
    def F(x):
        X = [(x[0] ** powers[i][0]) * (x[1] ** powers[i][1]) for i in range(len(a))]
        X = np.array(X)
        return np.dot(X, a) + a0
    return F
def plot_response_surface(F, y):
    x1 = np.linspace(14500., 15500.)
    x2 = np.linspace(28., 33.)
    z = [[F([x1i, x2i]) for x1i in x1] for x2i in x2]
    z = np.array(z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x1, x2 = np.meshgrid(x1, x2)
    ax.plot_surface(x1, x2, z, rstride=1, cstride=1, cmap='viridis', linewidth=0.3)
    x1 = np.linspace(14500, 15500, 6)
    x2 = np.linspace(28, 33, 6)
    x1, x2 = np.meshgrid(x1, x2)
    ax.scatter(x1, x2, y, c='r')
    plt.show()
if __name__ == '__main__':
    print('Reading input data')
    A, B, Y = read_input_data('aaa.csv')
    print('Constructing Simultaneous Linear Equations')
    dim = 2
    order = 2
    x, y, S, a, p = construct_equations(A, B, Y, dim, order)
    print('Computing Variance-Covariance Matrix Sjk and Sum of Deviation Vector M')
    S, M, x_bar, y_bar = compute_matrices(x, y, S, p)
    print('Computing Coefficient Vector a')
    a, a0 = compute_coefficients(S, M, x_bar, y_bar)
    print('Generating Polynomial Function F')
    powers = get_power(dim, order)
    F = generate_polynomial_function(a, a0, powers)
    print(f'a0: {a0:> 10e}')
    for i, ai in enumerate(a):
        print(f'a{i + 1}: {ai:> 10e}')
    print('Computing Coefficient of Determination')
    coef_of_determination(y, [F([x1, x2]) for x1, x2 in itertools.product(A, B)])
    print('Plotting Response Surface')
    plot_response_surface(F, y)