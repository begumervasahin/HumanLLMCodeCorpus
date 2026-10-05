def longest_common_subsequence(string1, string2):
    string1_chars = list(string1)
    string2_chars = list(string2)
    current_subsequence = []
    longest_subsequence = []
    for i in range(len(string1_chars)):
        for j in range(len(string2_chars)):
            if string1_chars[i] == string2_chars[j]:
                current_subsequence.append(string1_chars[i])
                i += 1
        if len(current_subsequence) > len(longest_subsequence):
            longest_subsequence = current_subsequence[:]
        current_subsequence.clear()
    longest_subsequence_str = ''.join(longest_subsequence)
    return longest_subsequence_str