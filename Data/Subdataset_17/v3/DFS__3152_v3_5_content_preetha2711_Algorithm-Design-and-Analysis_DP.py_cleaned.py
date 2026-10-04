def calculate_p(i, k):
    p = [[None] * (k + 1) for _ in range(i + 1)]
    for x in range(1, i + 1):
        for j in range(1, k + 1):
            if j == 1:
                p[x][j] = x
            elif j > x:
                p[x][j] = 0
            else:
                p[x][j] = p[x - 1][j] + p[x - 1][j - 1]
    return p[i][k]
def main():
    i = 1000
    k = 100
    result = calculate_p(i, k)
    print(f"The value of p[{i}][{k}] is: {result}")
if __name__ == "__main__":
    main()