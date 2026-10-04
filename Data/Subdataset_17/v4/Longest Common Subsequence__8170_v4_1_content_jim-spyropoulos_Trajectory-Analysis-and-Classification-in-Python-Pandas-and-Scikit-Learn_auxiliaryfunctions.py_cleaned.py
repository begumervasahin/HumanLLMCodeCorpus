import gmplot
from math import sin, cos, sqrt, atan2, radians
def haversine_np(point_a, point_b):
    R = 6373.0
    lat1, lon1 = radians(point_a[2]), radians(point_a[1])
    lat2, lon2 = radians(point_b[2]), radians(point_b[1])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
def compute_distances(trajectory):
    max_distance = 0.0
    total_distance = 0.0
    for i in range(len(trajectory) - 1):
        dist = haversine_np(trajectory[i], trajectory[i + 1])
        max_distance = max(max_distance, dist)
        total_distance += dist
    return total_distance, max_distance
def plot_traj(df_traj, plotname):
    latitudes = [point[2] for point in df_traj]
    longitudes = [point[1] for point in df_traj]
    gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 12)
    gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
    gmap.draw(f"{plotname}.html")
def plot_traj_red(com_points, df_traj, plotname):
    latitudes = [point[2] for point in df_traj]
    longitudes = [point[1] for point in df_traj]
    gmap = gmplot.GoogleMapPlotter(latitudes[0], longitudes[0], 12)
    gmap.plot(latitudes, longitudes, 'cornflowerblue', edge_width=10)
    latitudes = [point[2] for point in com_points]
    longitudes = [point[1] for point in com_points]
    gmap.plot(latitudes, longitudes, 'red', edge_width=10)
    gmap.draw(f"{plotname}.html")
def print_results(df_traj, distances, index, name):
    target_traj_coordinates = df_traj['timestamp_longitude_latitude'].iloc[index]
    target_journeypattid = df_traj['JourneyPatternId'].iloc[index]
    print(f"Traj: {target_journeypattid} Distance is {distances[index]:.4f} km.")
    plot_traj(target_traj_coordinates, name)
def lcss_trigger(traj, df, trigger, index):
    if trigger == 1:
        matching_points = []
        for elem in df['timestamp_longitude_latitude']:
            n0, n1 = len(traj), len(elem)
            C = [[0] * (n1 + 1) for _ in range(n0 + 1)]
            for i in range(1, n0 + 1):
                for j in range(1, n1 + 1):
                    if haversine_np(traj[i - 1], elem[j - 1]) <= 0.2:
                        C[i][j] = C[i - 1][j - 1] + 1
                    else:
                        C[i][j] = max(C[i][j - 1], C[i - 1][j])
            matching_points.append(C[n0][n1])
        return matching_points
    elif trigger == 2:
        common_points = []
        elem = df['timestamp_longitude_latitude'].iloc[index]
        n0, n1 = len(traj), len(elem)
        C = [[0] * (n1 + 1) for _ in range(n0 + 1)]
        for i in range(1, n0 + 1):
            for j in range(1, n1 + 1):
                if haversine_np(traj[i - 1], elem[j - 1]) <= 0.2:
                    C[i][j] = C[i - 1][j - 1] + 1
                    if elem[j - 1] not in common_points:
                        common_points.append(elem[j - 1])
                else:
                    C[i][j] = max(C[i][j - 1], C[i - 1][j])
        return common_points