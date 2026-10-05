def fonk1(start, end):
    b1 = [0, start]
    a1 = 2
    while b1[a1 - 1] + b1[a1 - 2] <= end:
        b1.append(b1[a1 - 1] + b1[a1 - 2])
        a1 += 1
    return b1
def fonk2(org_seq, target):
    b2 = None
    for b3 in org_seq:
        if b3 > target:
            break
        if b3 in (0, 1):
            continue
        if target % b3 = = 0:
            if b2 is None:
                b2 = target
            else:
                if target
                    b2 = target
    return b2 if b2 is not None else target
if b4 = = '__main__':
    a2 = 464
    b5 = fonk1(1, a2)
    b6 = fonk2(b5, a2)
    print(f"The minimum integer found is: {b6}")
    fonk1(b6, a2)