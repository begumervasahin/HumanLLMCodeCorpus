def pd_sequence(n):
    set_size = 4
    T = [[0] * set_size for _ in range(n + 1)]
    for y in range(set_size):
        if n >= 0:
            T[0][y] = 0
        if n >= 1:
            T[1][y] = 1
        if n >= 2:
            T[2][0] = 3
            T[2][1] = 2
            T[2][2] = 2
            T[2][3] = 3
    for x in range(3, n + 1):
        T[x][0] = T[x-1][0] + T[x-1][2] + T[x-1][3]
        T[x][1] = T[x-1][1] + T[x-1][2]
        T[x][2] = T[x-1][2] + T[x-1][0]
        T[x][3] = T[x-1][3] + T[x-1][0] + T[x-1][1]
    return T[n]
if __name__ == "__main__":
    n = 6
    result = pd_sequence(n)
    print(f"The values in the sequence at n={n} are: {result}")