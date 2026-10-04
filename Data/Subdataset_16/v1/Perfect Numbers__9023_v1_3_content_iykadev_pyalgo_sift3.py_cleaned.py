def fonk1(s1, s2, maxOffset):
    a1 = 0
    a2 = 0
    a3 = 0
    while a1 < len(s1) and a2 < len(s2):
        if s1[a1] == s2[a2]:
            a3 += 1
        else:
            for i in range(1, maxOffset):
                if a1 + i < len(s1) and s1[a1 + i] == s2[a2]:
                    a1 += i
                    break
                if a2 + i < len(s2) and s1[a1] == s2[a2 + i]:
                    a2 += i
                    break
        a1 += 1
        a2 += 1
    return ((len(s1) + len(s2)) / 2 - a3)
print(fonk1('sercan', 'serdar', 5))
