import gmplot
from math import sin, cos, sqrt, atan2, radians
def fonk1(pointa, pointb):
    a1 = 6373.0
    b1 = radians(pointa[2])
    b2 = radians(pointa[1])
    b3 = radians(pointb[2])
    b4 = radians(pointb[1])
    b5 = b4 - b2
    b6 = b3 - b1
    b7 = sin(b6 / 2) ** 2 + cos(b1) * cos(b3) * sin(b5 / 2) ** 2
    b8 = 2 * atan2(sqrt(b7), sqrt(1 - b7))
    b9 = a1 * b8
    return b9
def fonk2(trajectory):
    a2 = 0.0
    a3 = 0.0
    for i in range(0, len(trajectory) - 1):
        b10 = fonk1(trajectory[i], trajectory[i + 1])
        if b10 > a2:
            a2 = b10
        a3 += b10
    return [a3, a2]
def fonk3(df_traj, plotname):
    b11 = [point[1] for point in df_traj]
    b12 = [point[2] for point in df_traj]
    b13 = gmplot.GoogleMapPlotter(b12[0], b11[0], 12)
    b13.plot(b12, b11, 'cornflowerblue', b14 = 10)
    b13.draw(plotname + ".html")
def fonk4(com_points, df_traj, plotname):
    b11 = [point[1] for point in df_traj]
    b12 = [point[2] for point in df_traj]
    b13 = gmplot.GoogleMapPlotter(b12[0], b11[0], 12)
    b13.plot(b12, b11, 'cornflowerblue', b14 = 10)
    b15 = [point[1] for point in com_points]
    b16 = [point[2] for point in com_points]
    b13.plot(b16, b15, 'red', b14 = 10)
    b13.draw(plotname + ".html")
def fonk5(df_traj, distances, index, name):
    b17 = df_traj['timestamp_longitude_latitude'].iloc[index]
    b18 = df_traj['JourneyPatternId'].iloc[index]
    print(f"Traj: {b18} Distance is {distances[index]:.4f} km's.")
    fonk3(b17, name)
def fonk6(traj, df, b19, index):
    if b19 = = 1:
        b20 = []
        for b25 in df['timestamp_longitude_latitude']:
            b21 = len(traj)
            b22 = len(b25)
            b23 = [[0] * (b22 + 1) for _ in range(b21 + 1)]
            for i in range(1, b21 + 1):
                for j in range(1, b22 + 1):
                    if fonk1(traj[i - 1], b25[j - 1]) <= 0.2:
                        b23[i][j] = b23[i - 1][j - 1] + 1
                    else:
                        b23[i][j] = max(b23[i][j - 1], b23[i - 1][j])
            b20.append(b23[b21][b22])
        return b20
    elif b19 = = 2:
        b24 = []
        b25 = df['timestamp_longitude_latitude'].iloc[index]
        b21 = len(traj)
        b22 = len(b25)
        b23 = [[0] * (b22 + 1) for _ in range(b21 + 1)]
        for i in range(1, b21 + 1):
            for j in range(1, b22 + 1):
                if fonk1(traj[i - 1], b25[j - 1]) <= 0.2:
                    b23[i][j] = b23[i - 1][j - 1] + 1
                    if b25[j - 1] not in b24:
                        b24.append(b25[j - 1])
                else:
                    b23[i][j] = max(b23[i][j - 1], b23[i - 1][j])
        return b24
