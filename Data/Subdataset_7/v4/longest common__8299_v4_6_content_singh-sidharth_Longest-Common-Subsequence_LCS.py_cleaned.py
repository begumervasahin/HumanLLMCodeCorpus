def fonk1(str1, str2):
    b1 = len(str1)
    b2 = len(str2)
    b3 = [[0] * (b2 + 1) for _ in range(b1 + 1)]
    for i in range(1, b1 + 1):
        for j in range(1, b2 + 1):
            if str1[i - 1] == str2[j - 1]:
                b3[i][j] = b3[i - 1][j - 1] + 1
            else:
                b3[i][j] = max(b3[i - 1][j], b3[i][j - 1])
    return b3[b1][b2]
b4 = input("Enter the first string: ")
b5 = input("Enter the second string: ")
print("The length of the longest common subsequence is:", fonk1(b4, b5))