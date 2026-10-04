import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
def generate_poly_points(start, stop, num_points, coeff, noise_level=1, plot=True):
    x_pts = np.linspace(start, stop, num_points)
    y_pts = np.polyval(coeff[::-1], x_pts)
    if noise_level > 0:
        y_pts += np.random.normal(0, 10 ** noise_level, num_points)
    if plot:
        plt.figure()
        plt.scatter(x_pts, y_pts)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Generated Polynomial Points with Noise')
        plt.show()
    return x_pts, y_pts
if __name__ == "__main__":
    start = 0
    stop = 10
    num_points = 100
    coeff = [1, -2, 3]
    noise_level = 1
    plot = True
    x_pts, y_pts = generate_poly_points(start, stop, num_points, coeff, noise_level, plot)