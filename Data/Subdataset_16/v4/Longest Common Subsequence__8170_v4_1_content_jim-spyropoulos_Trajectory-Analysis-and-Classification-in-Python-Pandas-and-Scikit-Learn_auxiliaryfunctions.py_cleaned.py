import gmplot
from math import sin, cos, sqrt, atan2, radians
def fonk1(point_a, point_b):
    a1 = 6373.0
    lat1, b1 = radians(point_a[2]), radians(point_a[1])
    lat2, b2 = radians(point_b[2]), radians(point_b[1])
    b3 = b2 - b1
    b4 = lat2 - lat1
    b5 = sin(b4 / 2) ** 2 + cos(lat1) * cos(lat2) * sin(b3 / 2) ** 2
    b6 = 2 * atan2(sqrt(b5), sqrt(1 - b5))
    b7 = a1 * b6
    return b7
def fonk2(trajectory):
    a2 = 0.0
    a3 = 0.0
    for i in range(len(trajectory) - 1):
        b8 = fonk1(trajectory[i], trajectory[i + 1])
        a2 = max(a2, b8)
        a3 += b8
    return a3, a2
def fonk3(df_traj, plotname):
    b9 = [point[2] for point in df_traj]
    b10 = [point[1] for point in df_traj]
    b11 = gmplot.GoogleMapPlotter(b9[0], b10[0], 12)
    b11.plot(b9, b10, 'cornflowerblue', b12 = 10)
    b11.draw(f"{plotname}.html")
def fonk4(com_points, df_traj, plotname):
    b9 = [point[2] for point in df_traj]
    b10 = [point[1] for point in df_traj]
    b11 = gmplot.GoogleMapPlotter(b9[0], b10[0], 12)
    b11.plot(b9, b10, 'cornflowerblue', b12 = 10)
    b9 = [point[2] for point in com_points]
    b10 = [point[1] for point in com_points]
    b11.plot(b9, b10, 'red', b12 = 10)
    b11.draw(f"{plotname}.html")
def fonk5(df_traj, distances, index, name):
    b13 = df_traj['timestamp_longitude_latitude'].iloc[index]
    b14 = df_traj['JourneyPatternId'].iloc[index]
    print(f"Traj: {b14} Distance is {distances[index]:.4f} km.")
    fonk3(b13, name)
def fonk6(traj, df, b15, index):
    if b15 = = 1:
        b16 = []
        for b20 in df['timestamp_longitude_latitude']:
            n0, b17 = len(traj), len(b20)
            b18 = [[0] * (b17 + 1) for _ in range(n0 + 1)]
            for i in range(1, n0 + 1):
                for j in range(1, b17 + 1):
                    if fonk1(traj[i - 1], b20[j - 1]) <= 0.2:
                        b18[i][j] = b18[i - 1][j - 1] + 1
                    else:
                        b18[i][j] = max(b18[i][j - 1], b18[i - 1][j])
            b16.append(b18[n0][b17])
        return b16
    elif b15 = = 2:
        b19 = []
        b20 = df['timestamp_longitude_latitude'].iloc[index]
        n0, b17 = len(traj), len(b20)
        b18 = [[0] * (b17 + 1) for _ in range(n0 + 1)]
        for i in range(1, n0 + 1):
            for j in range(1, b17 + 1):
                if fonk1(traj[i - 1], b20[j - 1]) <= 0.2:
                    b18[i][j] = b18[i - 1][j - 1] + 1
                    if b20[j - 1] not in b19:
                        b19.append(b20[j - 1])
                else:
                    b18[i][j] = max(b18[i][j - 1], b18[i - 1][j])
        return b19