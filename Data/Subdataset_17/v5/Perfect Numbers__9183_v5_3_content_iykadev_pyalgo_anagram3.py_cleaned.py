def is_anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = [0] * 26
    count2 = [0] * 26
    for char in s1:
        count1[ord(char) - ord('a')] += 1
    for char in s2:
        count2[ord(char) - ord('a')] += 1
    return count1 == count2
print(is_anagram('pide', 'epid'))
