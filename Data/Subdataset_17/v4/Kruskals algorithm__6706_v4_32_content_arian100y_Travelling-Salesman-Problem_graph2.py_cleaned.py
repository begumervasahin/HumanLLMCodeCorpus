import matplotlib.pyplot as plt
from DynammicProgramming import *
def plot_route_with_info(reco, db, cost, time, xMedian, yMedian):
    x_coords = []
    y_coords = []
    for point in reco:
        x_coords.append(db[point[0]][0])
        y_coords.append(db[point[0]][1])
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords)
    plt.text(-84, -17.5, f"Distancia: {cost}")
    plt.text(-84, -19.5, f"Tiempo: {time}")
    plt.plot(x_coords, y_coords, '.')
    plt.plot(x_coords[0], y_coords[0], 'rx')
    plt.axhline(yMedian, color='black')
    plt.axvline(xMedian, color='black')
    plt.show()
plot_route_with_info(reco, db, cost, time, xMedian, yMedian)