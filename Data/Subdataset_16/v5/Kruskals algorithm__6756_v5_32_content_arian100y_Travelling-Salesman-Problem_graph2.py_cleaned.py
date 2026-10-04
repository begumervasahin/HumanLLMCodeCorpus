import matplotlib.pyplot as plt
from DynammicProgramming import *
def fonk1(recommended_points, coordinates_db, total_distance, total_time, x_median, y_median):
    b1 = [coordinates_db[point[0]][0] for point in recommended_points]
    b2 = [coordinates_db[point[0]][1] for point in recommended_points]
    b1.append(b1[0])
    b2.append(b2[0])
    plt.plot(b1, b2, b3 = "Route")
    plt.text(-84, -17.5, f"Distancia: {total_distance}")
    plt.text(-84, -19.5, f"Tiempo: {total_time}")
    plt.plot(b1, b2, 'o', b3 = "Points")
    plt.plot(b1[0], b2[0], 'rx', b3 = "Start Point")
    plt.axhline(y_median, b4 = 'black', linestyle='--', b3="Y Median")
    plt.axvline(x_median, b4 = 'black', linestyle='--', b3="X Median")
    plt.title("Route Visualization with Distance and Time Information")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.show()
fonk1(recommended_points, coordinates_db, total_distance, total_time, x_median, y_median)