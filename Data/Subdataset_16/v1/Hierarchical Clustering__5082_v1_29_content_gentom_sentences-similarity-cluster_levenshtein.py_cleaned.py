def fonk1(b10, b1):
    if len(b10) > len(b1):
        b10, b1 = b1, b10
    b2 = range(len(b10) + 1)
    for i2, c2 in enumerate(b1):
        b3 = [i2 + 1]
        for i1, b4 in enumerate(b10):
            if b4 = = c2:
                b3.append(b2[i1])
            else:
                b3.append(1 + min(
                    b2[i1],
                    b2[i1 + 1],
                    b3[-1]
                ))
        b2 = b3
    return b2[-1]
def fonk2(b10, b1):
    if len(b10) < len(b1):
        return fonk2(b1, b10)
    if len(b1) == 0:
        return len(b10)
    b5 = range(len(b1) + 1)
    for i, b4 in enumerate(b10):
        b6 = [i + 1]
        for j, c2 in enumerate(b1):
            b7 = b5[j + 1] + 1
            b8 = b6[j] + 1
            b9 = b5[j] + (b4 != c2)
            b6.append(min(b7, b8, b9))
        b5 = b6
    return b5[-1]
b10 = "kitten"
b1 = "sitting"
print(f"Edit distance between '{b10}' and '{b1}' using edit_distance function: {fonk1(b10, b1)}")
print(f"Edit distance between '{b10}' and '{b1}' using distance function: {fonk2(b10, b1)}")