import matplotlib.pyplot as plt
from DynammicProgramming import *
def fonk1(reco, db, cost, time, xMedian, yMedian):
    b1 = []
    b2 = []
    for point in reco:
        b1.append(db[point[0]][0])
        b2.append(db[point[0]][1])
    b1.append(b1[0])
    b2.append(b2[0])
    plt.plot(b1, b2)
    plt.text(-84, -17.5, f"Distancia: {cost}")
    plt.text(-84, -19.5, f"Tiempo: {time}")
    plt.plot(b1, b2, '.')
    plt.plot(b1[0], b2[0], 'rx')
    plt.axhline(yMedian, b3 = 'black')
    plt.axvline(xMedian, b3 = 'black')
    plt.show()
fonk1(reco, db, cost, time, xMedian, yMedian)