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
def fonk3(b1, b7):
    for path in b7:
        for connection in fonk1(path):
            b7.append([path])
    print(b7)
def fonk4(b1):
    b2 = []
    b3 = []
    for key, value in b1['v_start'].items():
        b2.append([key])
        b3.append(value)
    for path in b2:
        b4 = path[-1]
        if len(b1[b4].keys()) == 1:
            path.extend(b1[b4].keys())
            b3.append(b1[b4][list(b1[b4].keys())[0]])
        elif len(b1[b4].keys()) > 1:
            for key in b1[b4].keys():
                b5 = path.copy()
                b5.append(key)
                b2.append(b5)
    return b2, b3
if b6 = = '__main__':
    b7 = ['v_start']
    fonk3(b1, b7)
    b2, b3 = fonk4(b1)
    print("Paths:", b2)
    print("Weights:", b3)