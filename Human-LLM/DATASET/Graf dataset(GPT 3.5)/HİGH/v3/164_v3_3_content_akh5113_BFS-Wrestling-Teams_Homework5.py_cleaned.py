import collections
def fonk1(b11):
    b1 = {}
    with open(b11, "r") as f:
        b2 = f.readlines()
        b3 = int(b2[0])
        b4 = int(b2[b3 + 1])
        for line in b2[b3 + 2:]:
            wrestler1, b5 = line.strip().split()
            b1.setdefault(wrestler1, []).append(b5)
            b1.setdefault(b5, []).append(wrestler1)
    return b1
def fonk2(b1):
    b6 = []
    b7 = []
    b8 = collections.deque()
    for wrestler in b1:
        if wrestler not in b6 and wrestler not in b7:
            b6.append(wrestler)
            b8.append(wrestler)
            while b8:
                b9 = b8.popleft()
                for rival in b1[b9]:
                    if rival not in b6 and rival not in b7:
                        b7.append(rival)
                        b8.append(rival)
                    elif rival in b6:
                        return False, [], []
    return True, b6, b7
def fonk3(possible, b6, b7):
    if possible:
        print("Yes, it's possible")
        print("Baby Faces:", b6)
        print("Heels:", b7)
    else:
        print("No, it's not possible")
if b10 = = "__main__":
    b11 = "wrestler.txt"
    b1 = fonk1(b11)
    possible, b6, b7 = fonk2(b1)
    fonk3(possible, b6, b7)