def longest_common_subsequence(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    dp_matrix = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_matrix[i][j] = dp_matrix[i - 1][j - 1] + 1
            else:
                dp_matrix[i][j] = max(dp_matrix[i - 1][j], dp_matrix[i][j - 1])
    return dp_matrix[len_str1][len_str2]
first_string = input("First string: ")
second_string = input("Second string: ")
print("The length of the LCS is:", longest_common_subsequence(first_string, second_string))