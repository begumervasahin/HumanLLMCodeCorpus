def anagram(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for char in s1:
        pos = ord(char) - ord('a')
        c1[pos] += 1
    for char in s2:
        pos = ord(char) - ord('a')
        c2[pos] += 1
    for i in range(26):
        if c1[i] != c2[i]:
            return False
    return True
print(anagram('pide', 'epid'))
print(anagram('hello', 'bello'))
