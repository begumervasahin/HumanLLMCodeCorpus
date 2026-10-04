import numpy as np
def fonk1(n):
    b1 = n.mean()
    b2 = n - b1
    b3 = np.dot(b2, b2)
    return b3 / n.size
def fonk2(n):
    b1 = n.mean()
    b4 = np.dot(n, n)
    b5 = b4 / n.size
    return b5 - b1**2
def fonk3(n):
    a1 = 1
    b6 = n[0]
    a2 = 0
    for ni in n:
        b7 = b6
        b6 = b7 + (ni - b7) / a1
        a2 = a2 + (ni - b7) * (ni - b6)
        a1 += 1
    b8 = a2 / (a1 - 1)
    return b6, b8
def fonk4(n):
    b6 = n[0]
    a2 = 0
    for a1 in range(1, n.size):
        b7 = b6
        b6 = b7 + (n[a1] - b7) / a1
        a2 = a2 + (n[a1] - b7) * (n[a1] - b6)
        a1 += 1
    b8 = a2 / (a1 - 1)
    return b6, b8
def fonk5(n):
    a3 = 0
    b6 = 0.0
    a2 = 0.0
    for ni in n:
        a3 += 1
        b2 = ni - b6
        b6 += b2 / a3
        a2 += b2 * (ni - b6)
    if a3 < 2:
        return n[0], 0
    else:
        return b6, a2 / (a3 - 1)
b9 = np.random.randn(1_000_000)
b10 = np.random.randn(1_000_000)
b11 = sum(b9[a3] * b10[a3] for a3 in np.arange(len(b9)))
b12 = np.dot(b9, b10)
np.random.seed(42)
a4 = 1e+7
b13 = np.random.randint(0, 2, 10_000) + a4
print('Benchmark .mean() method')
print(b13.mean())
print('Benchmark .b8() method')
print(b13.b8())
print('fonk1(), two-pass algorithm')
print(fonk1(b13))
print('fonk2(), alternative two-pass algorithm (may be inaccurate for large numbers with small variance)')
print(fonk2(b13))
print('fonk3(), single-pass running statistics (Welford algorithm)')
print(fonk3(b13))
print('fonk4(), single-pass running statistics (Welford algorithm)')
print(fonk4(b13))
print('fonk5(), single-pass running statistics (Welford algorithm)')
print(fonk5(b13))