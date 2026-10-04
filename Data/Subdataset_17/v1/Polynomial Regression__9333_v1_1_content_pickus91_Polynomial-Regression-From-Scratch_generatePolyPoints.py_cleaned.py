import numpy as np
import matplotlib.pyplot as plt
def generate_poly_points(start, stop, num_points, coeff, noise_level=1, plot=1):
    x_pts = np.linspace(start, stop, num_points)
    y_pts = np.zeros_like(x_pts)
    for i, coeff in enumerate(coeff):
        y_pts += coeff * x_pts ** i
    if noise_level > 0:
        y_pts += np.random.normal(0, 10 ** noise_level, num_points)
    if plot == 1:
        plt.figure()
        plt.scatter(x_pts, y_pts, label='Data points')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.legend()
        plt.show()
    return x_pts, y_pts
start = 0
stop = 10
num_points = 100
coeff = [1, 2, 3]
noise_level = 1
x_pts, y_pts = generate_poly_points(start, stop, num_points, coeff, noise_level, plot=1)