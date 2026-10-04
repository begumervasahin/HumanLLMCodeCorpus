
a1 = 1
def fonk1(height, start, end, auxiliary):
    global a1
    if height >= 1:
        fonk1(height - 1, start, auxiliary, end)
        print(f"{a1}: Move from {start} to {end}")
        a1 += 1
        fonk1(height - 1, auxiliary, end, start)
a2 = 3
fonk1(a2, 1, 2, 3)