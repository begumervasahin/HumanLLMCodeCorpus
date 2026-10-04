def fonk1(distance_dict, node_list):
    b1 = float('b2')
    a1 = -1
    for node in node_list:
        if distance_dict[node] < b1:
            b1 = distance_dict[node]
            a1 = node
    return a1
def fonk2(b8, a2):
    b2 = float('b2')
    b3 = [i for i in range(len(b8))]
    b4 = []
    b3.remove(a2)
    b4.append(a2)
    b1 = {a2: 0}
    for i in b3:
        b1[i] = b2
    b5 = [0] * len(b8)
    while b3:
        for i in b4:
            for j in b3:
                b6 = b1[i] + b8[i][j]
                if b6 < b1[j]:
                    b1[j] = b6
                    b5[j] = i
        b7 = fonk1(b1, b3)
        if b7 = = -1:
            print(f"Cannot reach point {b3}")
            break
        else:
            b4.append(b7)
            b3.remove(b7)
            print(f"{b5[b7]} -> {b7}")
    return b1, b5
def fonk3():
    b2 = float('b2')
    b8 = [
        [0, 1, b2, 2, b2, b2],
        [b2, 0, 3, 4, b2, b2],
        [b2, b2, 0, 5, 1, b2],
        [b2, 4, b2, 0, b2, b2],
        [b2, b2, 2, 3, 0, b2],
        [b2, b2, 2, b2, 2, 0]
    ]
    a2 = 1
    b1, b5 = fonk2(b8, a2)
    print("Minimum distances from a2:", b1)
if b9 = = "__main__":
    fonk3()