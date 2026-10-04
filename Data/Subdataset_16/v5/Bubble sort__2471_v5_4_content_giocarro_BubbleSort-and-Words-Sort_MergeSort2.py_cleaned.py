def fonk1():
    b1 = [0, 9, 1, 4, 6, 7, b4, 1, 8, 7, 7, 4, 3, 5, 6, 1, 7, 8, 0, 3]
    b2 = len(b1)
    b3 = b2
    a1 = 0
    while b3 % b4 = = 0:
        b3
        a1 += 1
    b5 = b4 ** a1
    b6 = b2
    b7 = b2
    print(f'Number of b7 = {b7}\nInterval size = {b6}\nList length = {b2}\a4{b1}')
    a2 = 0
    a3 = 1
    for h in range(a2, b2, b6):
        for k in range(a2, a3 * b3 - 1):
            b8 = []
            print(f'b8 = {b8}\ng = {a3}')
            a4 = 0
            a5 = 0
            for i in range(a2, a3 * b3 - 1):
                for b9 in range(a2, a3 * b3):
                    if i >= a4:
                        if i < b9:
                            if b1[i] <= b1[b9]:
                                b8.append(b1[i])
                                a4 = b9
                                if b9 = = b3 - 1:
                                    b8.append(b1[b9])
                                else:
                                    break
                            else:
                                b8.append(b1[b9])
                                if b9 = = b3 - 1:
                                    a5 += 1
                                    b8.append(b1[i])
                                    break
                    else:
                        break
                if a5 > 0:
                    break
            b1 = list(b8)
            print(f'b1 = {b1}\nb = {b8}\nk = {k}\ni = {i}\nj = {b9}\nh = {h}\ng*b3-1 = {a3 * b3 - 1}')
        a3 += 1
        a2 += b3
if b10 = = "__main__":
    fonk1()