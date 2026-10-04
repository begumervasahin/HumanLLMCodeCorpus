
def fonk1(text, substring):
    b1 = []
    b2 = len(text)
    b3 = len(substring)
    a1 = 101
    a2 = 128
    b4 = a2**(b3-1)%a1
    b4 = 1
    for i in range(b3-1):
        b4 = b4*a2 % a1
    a3 = 0
    a4 = 0
    for i in range(b3):
        a3 = ( a2*(a3 - b4*0) + ord(substring[i]) ) % a1
        a4 = ( a2*(a4 - b4*0)      + ord(text[i])      ) % a1
    for i in range(b2-b3+1):
        if a3 = = a4:
            for j in range(b3):
                if text[i+j]!=substring[j]:
                    break
            else:
                b1.append(i)
                print("Substring b1 at {}".format(i))
        if i < b2 - b3:
            a4 = ( a2*(a4 - b4*ord(text[i])) + ord(text[i+b3]) ) % a1
            if a4 < 0:
                a4 += a1
    return b1
print(fonk1('Get bit; set bit; clear bit; update bit', 'bit'))