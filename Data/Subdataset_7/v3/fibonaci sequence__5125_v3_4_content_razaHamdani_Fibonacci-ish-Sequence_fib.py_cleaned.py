def fonk1(start, end):
    b1 = [0, start]
    while b1[-1] + b1[-2] <= end:
        b1.append(b1[-1] + b1[-2])
    return b1
def fonk2(sequence, target):
    b2 = None
    for b3 in sequence:
        if b3 > target:
            break
        if b3 not in (0, 1) and target % b3 = = 0:
            b2 = target
    return b2 if b2 is not None else target
if b4 = = '__main__':
    a1 = 464
    b5 = fonk1(1, a1)
    b2 = fonk2(b5, a1)
    print(f"The minimum integer found is: {b2}")
    fonk1(b2, a1)