import gmplot
from math import sin, cos, sqrt, atan2, radians
def fonk1(pointa, pointb):
    a1 = 6373.0
    lat1, b1 = radians(pointa[2]), radians(pointa[1])
    lat2, b2 = radians(pointb[2]), radians(pointb[1])
    dlon, b3 = b2 - b1, lat2 - lat1
    b4 = sin(b3 / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    b5 = 2 * atan2(sqrt(b4), sqrt(1 - b4))
    return a1 * b5
def fonk2(trajectory):
    total_distance, b6 = 0.0, 0.0
    for i in range(len(trajectory) - 1):
        b7 = fonk1(trajectory[i], trajectory[i + 1])
        total_distance += b7
        if b7 > b6:
            b6 = b7
    return total_distance, b6
def fonk3(trajectory, plotname):
    b8 = [point[1] for point in trajectory]
    b9 = [point[2] for point in trajectory]
    b10 = gmplot.GoogleMapPlotter(b9[0], b8[0], 12)
    b10.plot(b9, b8, 'cornflowerblue', b11 = 10)
    b10.draw(f"{plotname}.html")
def fonk4(b22, trajectory, plotname):
    b8 = [point[1] for point in trajectory]
    b9 = [point[2] for point in trajectory]
    b10 = gmplot.GoogleMapPlotter(b9[0], b8[0], 12)
    b10.plot(b9, b8, 'cornflowerblue', b11 = 10)
    b12 = [point[1] for point in b22]
    b13 = [point[2] for point in b22]
    b10.plot(b13, b12, 'red', b11 = 10)
    b10.draw(f"{plotname}.html")
def fonk5(df_traj, distances, b17, name):
    b14 = df_traj.iloc[b17]
    b15 = b14['timestamp_longitude_latitude']
    b16 = b14['JourneyPatternId']
    print(f"Traj: {b16} Distance is {distances[b17]:.4f} km's.")
    fonk3(b15, name)
def fonk6(traj, df, b18, b17 = None):
    if b18 = = 1:
        b19 = []
        for b23 in df['timestamp_longitude_latitude']:
            n0, b20 = len(traj), len(b23)
            b21 = [[0] * (b20 + 1) for _ in range(n0 + 1)]
            for i in range(1, n0 + 1):
                for j in range(1, b20 + 1):
                    if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                        b21[i][j] = b21[i - 1][j - 1] + 1
                    else:
                        b21[i][j] = max(b21[i][j - 1], b21[i - 1][j])
            b19.append(b21[n0][b20])
        return b19
    elif b18 = = 2 and b17 is not None:
        b22 = []
        b23 = df['timestamp_longitude_latitude'].iloc[b17]
        n0, b20 = len(traj), len(b23)
        b21 = [[0] * (b20 + 1) for _ in range(n0 + 1)]
        for i in range(1, n0 + 1):
            for j in range(1, b20 + 1):
                if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                    b21[i][j] = b21[i - 1][j - 1] + 1
                    if b23[j - 1] not in b22:
                        b22.append(b23[j - 1])
                else:
                    b21[i][j] = max(b21[i][j - 1], b21[i - 1][j])
        return b22
