def is_anagram(s1, s2):
    count_s1 = [0] * 26
    count_s2 = [0] * 26
    for char in s1:
        position = ord(char) - ord('a')
        count_s1[position] += 1
    for char in s2:
        position = ord(char) - ord('a')
        count_s2[position] += 1
    for index in range(26):
        if count_s1[index] != count_s2[index]:
            return False
    return True
print(is_anagram('pide', 'epid'))
