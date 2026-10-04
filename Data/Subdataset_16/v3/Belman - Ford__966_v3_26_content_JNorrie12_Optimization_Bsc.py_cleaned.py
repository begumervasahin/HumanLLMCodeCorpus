b1 = {
    "v_start": {"1_start": 0, "2_start": 0},
    "1_start": {"1_finish": 40},
    "2_start": {"2_finish": 36},
    "1_finish": {"v_finish": 0},
    "2_finish": {"v_finish": 0, "1_start": 0}
}
def fonk1(v_start):
    return b1.get(v_start, {})
def fonk2(start, finish):
    return b1.get(start, {}).get(finish, None)
def fonk3(b1, b4):
    for a1 in range(len(b4)):
        b2 = b4[a1]
        for j in fonk1(b2[-1]):
            b3 = b2 + [j]
            b4.append(b3)
    print(b4)
def fonk4(b1):
    b4 = []
    b5 = []
    for key, value in b1['v_start'].items():
        b4.append(['v_start', key])
        b5.append(value)
    a1 = 0
    while a1 < len(b4):
        b6 = b4[a1]
        b7 = b6[-1]
        b8 = fonk1(b7)
        if len(b8) == 1:
            b9 = next(iter(b8))
            b6.append(b9)
            b5.append(b8[b9])
        elif len(b8) > 1:
            for key in b8:
                b3 = b6 + [key]
                b4.append(b3)
        a1 += 1
    return b4, b5
if b10 = = '__main__':
    b11 = [['v_start']]
    fonk3(b1, b11)
    paths, b12 = fonk4(b1)
    print("Paths:", paths)
    print("Weights:", b12)