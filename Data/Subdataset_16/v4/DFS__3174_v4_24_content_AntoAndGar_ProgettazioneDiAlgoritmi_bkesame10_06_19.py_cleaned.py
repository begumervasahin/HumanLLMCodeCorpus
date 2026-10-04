def fonk1(length, b1 = 0, b2=None):
    if b2 is None:
        b2 = []
    if b1 = = length:
        print(''.join(b2))
        return
    for char in {'0', '1', '2', '3'}:
        if b1 = = 0 or (char != str(int(b2[b1 - 1]) + 1) and char != str(int(b2[b1 - 1]) - 1)):
            b2.append(char)
            fonk1(length, b1 + 1, b2)
            b2.pop()
fonk1(6)