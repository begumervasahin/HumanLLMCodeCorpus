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
for i in b2:
    b5 = b1[i[0]][0]
    b6 = b1[i[0]][1]
    b3.append(b5)
    b4.append(b6)
b3.append(b3[0])
b4.append(b4[0])
plt.plot(b3, b4)
plt.text(-84, -17.5, f"Distancia: {a1}")
plt.text(-84, -19.5, f"Tiempo: {a2}")
plt.plot(b3, b4, '.')
plt.plot(b3[0], b4[0], 'rx')
plt.axhline(a3, b7 = 'black')
plt.axvline(a4, b7 = 'black')
plt.show()