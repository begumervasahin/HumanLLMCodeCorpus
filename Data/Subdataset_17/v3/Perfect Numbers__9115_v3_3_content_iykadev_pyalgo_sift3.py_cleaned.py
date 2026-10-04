def sift3(s1, s2, max_offset):
    c1 = 0
    c2 = 0
    lcs = 0
    while c1 < len(s1) and c2 < len(s2):
        if s1[c1] == s2[c2]:
            lcs += 1
        else:
            offset_found = False
            for i in range(1, max_offset + 1):
                if c1 + i < len(s1) and s1[c1 + i] == s2[c2]:
                    c1 += i
                    offset_found = True
                    break
                if c2 + i < len(s2) and s1[c1] == s2[c2 + i]:
                    c2 += i
                    offset_found = True
                    break
            if not offset_found:
                c1 += 1
                c2 += 1
        else:
            c1 += 1
            c2 += 1
    average_length = (len(s1) + len(s2)) / 2
    sift3_distance = average_length - lcs
    return sift3_distance
print(sift3('sercan', 'serdar', 5))
