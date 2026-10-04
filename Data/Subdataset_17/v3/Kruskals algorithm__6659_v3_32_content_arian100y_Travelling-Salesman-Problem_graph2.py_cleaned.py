import matplotlib.pyplot as plt
def plot_path_with_annotations(db, reco, cost, time, x_median, y_median):
    x_coords = []
    y_coords = []
    for start, end in reco:
        x_coords.append(db[start][0])
        y_coords.append(db[start][1])
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])
    plt.plot(x_coords, y_coords, label='Path')
    plt.text(x_median - 0.2, y_median - 0.2, f"Distancia: {cost}")
    plt.text(x_median - 0.2, y_median - 0.4, f"Tiempo: {time}")
    plt.plot(x_coords, y_coords, 'o', label='Points')
    plt.plot(x_coords[0], y_coords[0], 'rx', label='Start Point')
    plt.axhline(y_median, color='black', linestyle='--', label='Y Median')
    plt.axvline(x_median, color='black', linestyle='--', label='X Median')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    db = {
        0: (-84.1, -17.6),
        1: (-83.9, -17.4),
        2: (-83.8, -17.3),
    }
    reco = [(0, 1), (1, 2), (2, 0)]
    cost = 100
    time = 10
    y_median = -17.5
    x_median = -84.0
    plot_path_with_annotations(db, reco, cost, time, x_median, y_median)