import numpy as np
import matplotlib.pyplot as plt
def generate_poly_points(start, stop, num_points, coeff, noise_level=1, plot=1):
    x_pts = np.linspace(start, stop, num_points)
    y_pts = np.polyval(coeff[::-1], x_pts)
    if noise_level > 0:
        noise = np.random.normal(0, 10 ** noise_level, num_points)
        y_pts += noise
    if plot == 1:
        plt.figure()
        plt.scatter(x_pts, y_pts, label='Data points')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.legend()
        plt.show()
    return x_pts, y_pts
if __name__ == "__main__":
    start = 0
    stop = 10
    num_points = 100
    coeff = [1, 2, 3]
    noise_level = 1
    x_pts, y_pts = generate_poly_points(start, stop, num_points, coeff, noise_level, plot=1)