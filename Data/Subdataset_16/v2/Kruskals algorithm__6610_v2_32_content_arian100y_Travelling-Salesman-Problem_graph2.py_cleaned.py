import matplotlib.pyplot as plt
b1 = {
    0: (-84.1, -17.6),
    1: (-83.9, -17.4),
    2: (-83.8, -17.3),
}
b2 = [(0, 1), (1, 2), (2, 0)]
a1 = 100
a2 = 10
a3 = -17.5
a4 = -84.0
b3 = []
b4 = []
for start, end in b2:
    b3.append(b1[start][0])
    b4.append(b1[start][1])
b3.append(b3[0])
b4.append(b4[0])
plt.plot(b3, b4, b5 = 'Path')
plt.text(a4 - 0.2, a3 - 0.2, f"Distancia: {a1}")
plt.text(a4 - 0.2, a3 - 0.4, f"Tiempo: {a2}")
plt.plot(b3, b4, 'o', b5 = 'Points')
plt.plot(b3[0], b4[0], 'rx', b5 = 'Start Point')
plt.axhline(a3, b6 = 'black', linestyle='--', b5='Y Median')
plt.axvline(a4, b6 = 'black', linestyle='--', b5='X Median')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()