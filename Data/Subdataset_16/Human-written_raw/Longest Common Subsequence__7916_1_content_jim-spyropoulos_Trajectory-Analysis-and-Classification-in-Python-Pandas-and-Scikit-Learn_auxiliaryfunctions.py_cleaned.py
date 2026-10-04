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
        a4 = 0.0
        a4 = fonk1(trajectory[i], trajectory[i + 1])
        if a4 > a2:
            a2 = a4
        a3 += a4
    return [a3, a2]
def fonk3(df_traj, plotname):
    b10 = []
    b11 = []
    for elem2 in df_traj:
        b10.append(elem2[1])
        b11.append(elem2[2])
    b12 = gmplot.GoogleMapPlotter(b11[0], b10[0], len(df_traj))
    b12.plot(b11, b10, 'cornflowerblue', b13 = 10)
    b12.draw(plotname + ".html")
def fonk4(com_points, df_traj, plotname):
    b10 = []
    b11 = []
    for elem2 in df_traj:
        b10.append(elem2[1])
        b11.append(elem2[2])
    b12 = gmplot.GoogleMapPlotter(b11[0], b10[0], 12)
    b12.plot(b11, b10, 'cornflowerblue', b13 = 10)
    b10 = []
    b11 = []
    for elem2 in com_points:
        b10.append(elem2[1])
        b11.append(elem2[2])
    b12.plot(b11, b10, 'red', b13 = 10)
    b12.draw(plotname + ".html")
def fonk5(df_traj, distances, index, name):
    b14 = df_traj['timestamp_longitude_latitude'].iloc[index]
    b15 = df_traj['JourneyPatternId'].iloc[index]
    print
    "Traj: " + str(b15) + "Distance is %.4f km's." % distances[index]
    fonk3(b14, name)
def fonk6(traj, df, b16, index):
    if (b16 = = 1):
        b17 = []
        b18 = 0;
        for b23 in df['timestamp_longitude_latitude']:
            b19 = len(traj)
            b20 = len(b23)
            b21 = [[0] * (b20 + 1) for _ in range(b19 + 1)]
            for i in range(1, b19 + 1):
                for j in range(1, b20 + 1):
                    if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                        b21[i][j] = b21[i - 1][j - 1] + 1
                    else:
                        b21[i][j] = max(b21[i][j - 1], b21[i - 1][j])
            b17.append(b21[b19][b20])
            b18 = b18 + 1
    elif (b16 = = 2):
        b22 = []
        b23 = df['timestamp_longitude_latitude'].iloc[index]
        b19 = len(traj)
    b20 = len(b23)
    b21 = [[0] * (b20 + 1) for _ in range(b19 + 1)]
    for i in range(1, b19 + 1):
        for j in range(1, b20 + 1):
            if fonk1(traj[i - 1], b23[j - 1]) <= 0.2:
                b21[i][j] = b21[i - 1][j - 1] + 1
                if (b23[j - 1] not in b22):
                    b22.append(b23[j - 1])
            else:
                b21[i][j] = max(b21[i][j - 1], b21[i - 1][j])
    if (b16 = = 1):
        return b17
    else:
        return b22