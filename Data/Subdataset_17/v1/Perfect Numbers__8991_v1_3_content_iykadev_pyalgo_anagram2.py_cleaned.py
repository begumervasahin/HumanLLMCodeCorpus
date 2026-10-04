def anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    alist1 = list(s1)
    alist2 = list(s2)
    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(alist1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches
if __name__ == "__main__":
    result = anagram('ey edip', 'pide ye')
    print(result)
