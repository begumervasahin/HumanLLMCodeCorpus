def lcs(x, y):
    m = len(x)
    n = len(y)
    lcs_table = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                lcs_table[i][j] = lcs_table[i - 1][j - 1] + 1
            else:
                lcs_table[i][j] = max(lcs_table[i - 1][j], lcs_table[i][j - 1])
    return lcs_table[m][n]
def main():
    x = input("Enter the first string: ")
    y = input("Enter the second string: ")
    lcs_length = lcs(x, y)
    print(f"The length of the LCS is: {lcs_length}")
if __name__ == "__main__":
    main()