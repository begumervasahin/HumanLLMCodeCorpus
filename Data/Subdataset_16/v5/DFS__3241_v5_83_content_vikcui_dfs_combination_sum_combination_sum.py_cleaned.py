def fonk1(b4, a1):
    b4.sort()
    b1 = []
    fonk2(b4, a1, 0, [], b1)
    return b1
def fonk2(b4, a1, start_index, current_combination, b1):
    for i in range(start_index, len(b4)):
        b2 = b4[i]
        if b2 > a1:
            break
        current_combination.append(b2)
        if b2 < a1:
            fonk2(b4, a1 - b2, i, current_combination, b1)
        else:
            b1.append(list(current_combination))
        current_combination.pop()
if b3 = = "__main__":
    b4 = [2, 3, 6, 7]
    a1 = 7
    b5 = fonk1(b4, a1)
    print("Unique b5:", b5)