def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = [0] * 26
    count2 = [0] * 26
    for char in s1:
        index = ord(char) - ord('a')
        count1[index] += 1
    for char in s2:
        index = ord(char) - ord('a')
        count2[index] += 1
    for i in range(26):
        if count1[i] != count2[i]:
            return False
    return True
print(is_anagram('pide', 'epid'))
