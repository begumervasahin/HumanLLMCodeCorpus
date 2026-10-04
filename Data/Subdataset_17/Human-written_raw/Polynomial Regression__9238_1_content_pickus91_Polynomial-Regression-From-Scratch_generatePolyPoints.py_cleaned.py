
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
def generatePolyPoints(start, stop, num_points, coeff, noiseLevel = 1, plot = 1):
    x_pts = np.arange(start, stop, (stop - start)/num_points)
    line = coeff[0]
    for i in np.arange(1, len(coeff)):
        line += coeff[i] * x_pts ** i
    if noiseLevel > 0:
        y_pts = np.random.normal(-(10 ** noiseLevel), 10 ** noiseLevel, len(x_pts)) + line
    else:
        y_pts = line
    if plot == 1:
        plt.figure()
        plt.scatter(x_pts, y_pts)
        plt.xlabel('x')
        plt.ylabel('y')
    return x_pts, y_pts