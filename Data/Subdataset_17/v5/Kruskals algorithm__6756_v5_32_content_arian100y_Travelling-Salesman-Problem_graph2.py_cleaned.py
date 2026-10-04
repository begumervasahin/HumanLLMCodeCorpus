import matplotlib.pyplot as plt
from DynammicProgramming import *
def plot_route_with_info(recommended_points, coordinates_db, total_distance, total_time, x_median, y_median):
    x_coords = [coordinates_db[point[0]][0] for point in recommended_points]
    y_coords = [coordinates_db[point[0]][1] for point in recommended_points]
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords, label="Route")
    plt.text(-84, -17.5, f"Distancia: {total_distance}")
    plt.text(-84, -19.5, f"Tiempo: {total_time}")
    plt.plot(x_coords, y_coords, 'o', label="Points")
    plt.plot(x_coords[0], y_coords[0], 'rx', label="Start Point")
    plt.axhline(y_median, color='black', linestyle='--', label="Y Median")
    plt.axvline(x_median, color='black', linestyle='--', label="X Median")
    plt.title("Route Visualization with Distance and Time Information")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.show()
plot_route_with_info(recommended_points, coordinates_db, total_distance, total_time, x_median, y_median)