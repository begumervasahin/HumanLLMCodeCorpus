a1 = 1
def fonk1(h, initial, end, aux):
    global a1
    if h >= 1:
        fonk1(h - 1, initial, aux, end)
        print(a1, ": ", "Move from ", initial, " to ", end)
        a1 += 1
        fonk1(h - 1, aux, end, initial)
fonk1(3, 1, 2, 3)