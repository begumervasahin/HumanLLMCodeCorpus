
n = 5
T = [0 for _ in range(n + 1)]
def PD(n):
    T[0] = 1
    T[1] = 4
    T[2] = 10
    for i in range(3, n + 1):
        T[i] = 3 * T[i - 1] - T[i - 2]
    return T[n]
print(PD(n))