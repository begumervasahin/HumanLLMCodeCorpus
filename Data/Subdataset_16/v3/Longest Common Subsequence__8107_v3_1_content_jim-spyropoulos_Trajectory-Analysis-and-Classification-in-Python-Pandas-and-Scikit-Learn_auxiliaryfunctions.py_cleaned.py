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
        b6 = max(b6, b7)
    return total_distance, b6
def fonk3(trajectory, plotname, b8 = None):
    b9 = [point[1] for point in trajectory]
    b10 = [point[2] for point in trajectory]
    b11 = gmplot.GoogleMapPlotter(b10[0], b9[0], 12)
    b11.plot(b10, b9, 'cornflowerblue', b12 = 10)
    if b8:
        b13 = [point[1] for point in b8]
        b14 = [point[2] for point in b8]
        b11.plot(b14, b13, 'red', b12 = 10)
    b11.draw(f"{plotname}.html")
def fonk4(df_traj, distances, b18, plotname):
    b15 = df_traj.iloc[b18]
    b16 = b15['timestamp_longitude_latitude']
    b17 = b15['JourneyPatternId']
    print(f"Traj: {b17} Distance is {distances[b18]:.4f} km's.")
    fonk3(b16, plotname)
def fonk5(traj, df, b19, b18 = None):
    if b19 = = 1:
        b20 = []
        for b23 in df['timestamp_longitude_latitude']:
            n0, b21 = len(traj), len(b23)
            b22 = [[0] * (b21 + 1) for _ in range(n0 + 1)]
            for i in range(1, n0 + 1):
                for j in range(1, b21 + 1):
                    if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                        b22[i][j] = b22[i - 1][j - 1] + 1
                    else:
                        b22[i][j] = max(b22[i][j - 1], b22[i - 1][j])
            b20.append(b22[n0][b21])
        return b20
    elif b19 = = 2 and b18 is not None:
        b8 = []
        b23 = df['timestamp_longitude_latitude'].iloc[b18]
        n0, b21 = len(traj), len(b23)
        b22 = [[0] * (b21 + 1) for _ in range(n0 + 1)]
        for i in range(1, n0 + 1):
            for j in range(1, b21 + 1):
                if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                    b22[i][j] = b22[i - 1][j - 1] + 1
                    if b23[j - 1] not in b8:
                        b8.append(b23[j - 1])
                else:
                    b22[i][j] = max(b22[i][j - 1], b22[i - 1][j])
        return b8
