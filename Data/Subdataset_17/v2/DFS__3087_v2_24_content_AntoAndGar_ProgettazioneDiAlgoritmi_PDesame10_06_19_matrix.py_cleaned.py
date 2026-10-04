def pd_sequence(n):
    set_size = 4
    T = [[0 for _ in range(set_size)] for _ in range(n + 1)]
    for x in range(n + 1):
        for y in range(set_size):
            if x == 0:
                T[x][y] = 0
            elif x == 1:
                T[x][y] = 1
            elif x == 2:
                T[x][0] = 3
                T[x][1] = 2
                T[x][2] = 2
                T[x][3] = 3
            else:
                if y == 0:
                    T[x][y] = T[x-1][y] + T[x-1][y+2] + T[x-1][y+3]
                elif y == 1:
                    T[x][y] = T[x-1][y] + T[x-1][y+2]
                elif y == 2:
                    T[x][y] = T[x-1][y] + T[x-1][y-2]
                elif y == 3:
                    T[x][y] = T[x-1][y] + T[x-1][y-2] + T[x-1][y-3]
    return T[n]
if __name__ == "__main__":
    n = 6
    result = pd_sequence(n)
    print(f"The values in the sequence at n={n} are: {result}")