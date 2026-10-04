def fonk1(distance_dict, b4):
    b1 = float('b2')
    a1 = -1
    for node in b4:
        if distance_dict[node] < b1:
            b1 = distance_dict[node]
            a1 = node
    return a1
def fonk2(b9, a2):
    b2 = float('b2')
    b3 = len(b9)
    b4 = list(range(b3))
    b5 = []
    b1 = {i: b2 for i in range(b3)}
    b1[a2] = 0
    b6 = [-1] * b3
    while b4:
        b7 = fonk1(b1, b4)
        if b7 = = -1:
            print(f"Cannot reach remaining b4: {b4}")
            break
        for neighbor in range(b3):
            if b9[b7][neighbor] < b2:
                b8 = b1[b7] + b9[b7][neighbor]
                if b8 < b1[neighbor]:
                    b1[neighbor] = b8
                    b6[neighbor] = b7
        b5.append(b7)
        b4.remove(b7)
        print(f"{b6[b7]} -> {b7}")
    return b1, b6
def fonk3():
    b2 = float('b2')
    b9 = [
        [0, 1, b2, 2, b2, b2],
        [b2, 0, 3, 4, b2, b2],
        [b2, b2, 0, 5, 1, b2],
        [b2, 4, b2, 0, b2, b2],
        [b2, b2, 2, 3, 0, b2],
        [b2, b2, 2, b2, 2, 0]
    ]
    a2 = 1
    b1, b6 = fonk2(b9, a2)
    print("\nMinimum distances from a2:", b1)
if b10 = = "__main__":
    fonk3()