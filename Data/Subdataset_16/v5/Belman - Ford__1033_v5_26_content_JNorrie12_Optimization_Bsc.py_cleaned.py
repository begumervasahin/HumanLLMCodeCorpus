b1 = {
    "v_start": {"1_start": 0, "2_start": 0},
    "1_start": {"1_finish": 40},
    "2_start": {"2_finish": 36},
    "1_finish": {"v_finish": 0},
    "2_finish": {"v_finish": 0, "1_start": 0}
}
def fonk1(node):
    return b1.get(node, {})
def fonk2(start, finish):
    return b1.get(start, {}).get(finish, None)
def fonk3(b1, b9):
    for path in b9:
        for connection in fonk1(path):
            b9.append([path])
    print(b9)
def fonk4(b1):
    b2 = []
    b3 = []
    for key, value in b1['v_start'].items():
        b2.append([key])
        b3.append(value)
    for path in b2:
        b4 = path[-1]
        b5 = b1[b4]
        if len(b5) == 1:
            b6 = list(b5.keys())[0]
            path.append(b6)
            b3.append(b5[b6])
        elif len(b5) > 1:
            for key in b5.keys():
                b7 = path.copy()
                b7.append(key)
                b2.append(b7)
    return b2, b3
if b8 = = '__main__':
    b9 = ['v_start']
    fonk3(b1, b9)
    b2, b3 = fonk4(b1)
    print("Paths:", b2)
    print("Weights:", b3)