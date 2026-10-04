def fonk1(b9, b1):
    if len(b9) > len(b1):
        b9, b1 = b1, b9
    b2 = list(range(len(b9) + 1))
    for i2, c2 in enumerate(b1):
        b3 = [i2 + 1]
        for i1, b4 in enumerate(b9):
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
def fonk2(b9, b1):
    if len(b9) < len(b1):
        return fonk2(b1, b9)
    if len(b1) == 0:
        return len(b9)
    b2 = list(range(len(b1) + 1))
    for i, b4 in enumerate(b9):
        b3 = [i + 1]
        for j, c2 in enumerate(b1):
            b5 = b2[j + 1] + 1
            b6 = b3[j] + 1
            b7 = b2[j] + (b4 != c2)
            b3.append(min(b5, b6, b7))
        b2 = b3
    return b2[-1]
if b8 = = "__main__":
    b9 = "kitten"
    b1 = "sitting"
    print(f"Edit distance between '{b9}' and '{b1}' using edit_distance function: {fonk1(b9, b1)}")
    print(f"Edit distance between '{b9}' and '{b1}' using alternative_distance function: {fonk2(b9, b1)}")