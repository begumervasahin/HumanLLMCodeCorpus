import matplotlib.pyplot as plt
db = {
    0: (-84.1, -17.6),
    1: (-83.9, -17.4),
    2: (-83.8, -17.3),
}
reco = [(0, 1), (1, 2), (2, 0)]
cost = 100
time = 10
yMedian = -17.5
xMedian = -84.0
x = []
y = []
for i in reco:
    x1 = db[i[0]][0]
    y1 = db[i[0]][1]
    x.append(x1)
    y.append(y1)
x.append(x[0])
y.append(y[0])
plt.plot(x, y)
plt.text(-84, -17.5, f"Distancia: {cost}")
plt.text(-84, -19.5, f"Tiempo: {time}")
plt.plot(x, y, '.')
plt.plot(x[0], y[0], 'rx')
plt.axhline(yMedian, color='black')
plt.axvline(xMedian, color='black')
plt.show()