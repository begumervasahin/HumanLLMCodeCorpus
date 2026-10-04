import matplotlib.pyplot as plt
def fonk1(b6, b7, a1, a2, a4, a3):
    b1 = []
    b2 = []
    for start, end in b7:
        b1.append(b6[start][0])
        b2.append(b6[start][1])
    b1.append(b1[0])
    b2.append(b2[0])
    plt.plot(b1, b2, b3 = 'Path')
    plt.text(a4 - 0.2, a3 - 0.2, f"Distancia: {a1}")
    plt.text(a4 - 0.2, a3 - 0.4, f"Tiempo: {a2}")
    plt.plot(b1, b2, 'o', b3 = 'Points')
    plt.plot(b1[0], b2[0], 'rx', b3 = 'Start Point')
    plt.axhline(a3, b4 = 'black', linestyle='--', b3='Y Median')
    plt.axvline(a4, b4 = 'black', linestyle='--', b3='X Median')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()
if b5 = = "__main__":
    b6 = {
        0: (-84.1, -17.6),
        1: (-83.9, -17.4),
        2: (-83.8, -17.3),
    }
    b7 = [(0, 1), (1, 2), (2, 0)]
    a1 = 100
    a2 = 10
    a3 = -17.5
    a4 = -84.0
    fonk1(b6, b7, a1, a2, a4, a3)