def fonk1(s1, s2, max_offset):
    c1, c2, b1 = 0, 0, 0
    while c1 < len(s1) and c2 < len(s2):
        if s1[c1] == s2[c2]:
            b1 += 1
        else:
            for i in range(1, max_offset):
                if c1 + i < len(s1) and s1[c1 + i] == s2[c2]:
                    c1 += i
                    break
                if c2 + i < len(s2) and s1[c1] == s2[c2 + i]:
                    c2 += i
                    break
        c1 += 1
        c2 += 1
    return (len(s1) + len(s2)) / 2 - b1
print(fonk1('sercan', 'serdar', 5))
