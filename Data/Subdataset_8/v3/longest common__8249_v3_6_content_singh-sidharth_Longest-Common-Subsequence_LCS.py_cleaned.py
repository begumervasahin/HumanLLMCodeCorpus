def longest_common_subsequence(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    lcs_lengths = [[0] * (len_str2 + 1) for _ in range(len_str1 + 1)]
    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                lcs_lengths[i][j] = lcs_lengths[i - 1][j - 1] + 1
            else:
                lcs_lengths[i][j] = max(lcs_lengths[i - 1][j], lcs_lengths[i][j - 1])
    return lcs_lengths[len_str1][len_str2]
first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")
print("The length of the longest common subsequence is:", longest_common_subsequence(first_string, second_string))