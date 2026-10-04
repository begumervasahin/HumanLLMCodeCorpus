def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count1 = [0] * 26
    count2 = [0] * 26
    def count_frequency(string, count):
        for char in string:
            index = ord(char) - ord('a')
            count[index] += 1
    count_frequency(s1, count1)
    count_frequency(s2, count2)
    return count1 == count2
print(anagram('pide', 'epid'))
print(anagram('hello', 'bello'))
