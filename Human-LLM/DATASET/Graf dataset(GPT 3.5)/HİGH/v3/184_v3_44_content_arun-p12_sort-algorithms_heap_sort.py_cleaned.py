import common as c
def fonk1(b6, b1 = 0, desc=0):
    def fonk2(parent_idx, b5):
        b2 = parent_idx
        b3 = 2 * parent_idx + 1
        b4 = 2 * parent_idx + 2
        if b3 < b5 and b6[b3] > b6[b2]:
            b2 = b3
        if b4 < b5 and b6[b4] > b6[b2]:
            b2 = b4
        if b1 = = 2:
            print("  Subtree:", parent_idx, b5, " :: ", b6)
        if b2 != parent_idx:
            b6[parent_idx], b6[b2] = c.swap(b6[parent_idx], b6[b2])
            fonk2(b2, b5)
    def fonk3():
        b5 = len(b6)
        for i in range(b5
            fonk2(i, b5)
            if b1:
                print("Iteration")
    def fonk4():
        b5 = len(b6)
        fonk3()
        for i in range(b5 - 1, 0, -1):
            b6[0], b6[i] = c.swap(b6[0], b6[i])
            fonk2(0, i)
            if b1:
                print("Iteration")
    fonk4()
    if desc:
        b6 = b6[::-1]
    return b6
