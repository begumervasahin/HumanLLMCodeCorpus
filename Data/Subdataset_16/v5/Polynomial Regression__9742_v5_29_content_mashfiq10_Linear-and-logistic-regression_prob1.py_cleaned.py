import numpy as np
import matplotlib.pyplot as plt
b1 = np.loadtxt("crash.txt")
b2 = b1[1::2]
b3 = b1[0:-1:2]
b4 = b2[:, 0].reshape(-1, 1)
b5 = b2[:, 1].reshape(-1, 1)
b6 = b3[:, 0].reshape(-1, 1)
b7 = b3[:, 1].reshape(-1, 1)
a1 = 20
b8 = np.zeros(a1)
b9 = np.zeros(a1)
b10 = {"Erms": float('inf'), "L": 0, "b13": None}
b11 = {"Erms": float('inf'), "L": 0, "b13": None}
def fonk1(x, degree):
    return np.hstack([x ** i for i in range(degree)])
for L in range(1, a1 + 1):
    b12 = fonk1(b4, L)
    b13 = np.linalg.solve(b12.T @ b12, b12.T @ b5)
    b14 = 0.5 * np.square(np.linalg.norm(b5 - b12 @ b13))
    b8[L-1] = np.sqrt(2.0 * b14 / len(b2))
    if b8[L-1] < b10["Erms"]:
        b10["Erms"] = b8[L-1]
        b10["L"] = L
        b10["b13"] = b13
    b15 = fonk1(b6, L)
    b16 = 0.5 * np.square(np.linalg.norm(b7 - b15 @ b13))
    b9[L-1] = np.sqrt(2.0 * b16 / len(b3))
    if b9[L-1] < b11["Erms"]:
        b11["Erms"] = b9[L-1]
        b11["L"] = L
        b11["b13"] = b13
print('Maximum likelihood RMS error between the actual b1 and the model\'s prediction (for Training sets): \n', b8)
print('Maximum likelihood RMS error between the actual b1 and the model\'s prediction (for Test sets): \n', b9)
plt.figure(b17 = (16, 12))
plt.plot(b8, '-o', b18 = 'none', color='b', b23='Training')
plt.plot(b9, '-o', b18 = 'none', color='r', b23='Test')
plt.suptitle('Maximum likelihood RMS error between the actual b1 and the model\'s prediction', b19 = 24)
plt.legend(b19 = 22)
plt.xlabel("Polynomial Degree (M)", b19 = 22)
plt.ylabel("Erms", b19 = 22)
plt.show()
def fonk2(x, t, title, best_model):
    b20 = np.linspace(np.min(x), np.max(x), 100).reshape(-1, 1)
    b21 = fonk1(b20, best_model["L"])
    b22 = b21 @ best_model["b13"]
    plt.figure(b17 = (16, 12))
    plt.plot(x, t, 'bo', b23 = 'Data')
    plt.plot(b20, b22, 'r-', b23 = 'Best fit model')
    plt.suptitle(title, b19 = 24)
    plt.legend(b19 = 22)
    plt.xlabel("Time", b19 = 22)
    plt.ylabel("Acceleration", b19 = 22)
    plt.show()
print('Lowest RMS L for b2 b1:', b10["L"])
fonk2(b4, b5, 'Best fit on the b2 set', b10)
print('Lowest RMS L for b3 b1:', b11["L"])
fonk2(b6, b7, 'Best fit on the b3 set', b11)