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
    b2 = b1.get(start, {})
    return b2.get(finish, None)
def fonk3(b1, b3):
    for i in b3:
        for j in fonk1(i):
            b3.append([i])
    print(b3)
def fonk4(b1):
    b3 = []
    b4 = []
    for key, value in b1['v_start'].items():
        b3.append([key])
        b4.append(value)
    for path in b3:
        b5 = path[-1]
        if len(b1[b5].keys()) == 1:
            path.extend(b1[b5].keys())
            b4.extend(b1[b5].values())
        elif len(b1[b5].keys()) > 1:
            for key in b1[b5].keys():
                b6 = path.copy()
                b6.append(key)
                b3.append(b6)
    return b3, b4
if b7 = = '__main__':
    b3 = ['v_start']
    fonk3(b1, b3)
    paths, b8 = fonk4(b1)
    print("Paths:", paths)
    print("Weights:", b8)