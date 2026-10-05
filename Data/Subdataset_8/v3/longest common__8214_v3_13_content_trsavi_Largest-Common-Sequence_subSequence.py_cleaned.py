def longest_common_subsequence(str1, str2):
    str1_chars = list(str1)
    str2_chars = list(str2)
    current_subsequence = []
    longest_subsequence = []
    for start_index in range(len(str1_chars) + 1):
        current_subsequence = []
        for char in str1_chars[start_index:]:
            if char in str2_chars:
                current_subsequence.append(char)
                index = str2_chars.index(char) + 1
                str2_chars = str2_chars[index:]
        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence
        str2_chars = list(str2)
    result = ''.join(longest_subsequence)
    return result
print(longest_common_subsequence('ABCABA', 'ABBA'))
print(longest_common_subsequence('aaaaa', 'aa'))
print(longest_common_subsequence('AGGTAB', 'GXTXAYB'))
print(longest_common_subsequence('ABAZDC', 'BACBAD'))
