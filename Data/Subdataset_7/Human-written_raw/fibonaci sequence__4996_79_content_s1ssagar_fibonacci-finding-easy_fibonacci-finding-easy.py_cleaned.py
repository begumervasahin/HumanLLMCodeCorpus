def fonk1(mat1, mat2):
    b1 = ((10**9)+7)
    return [((mat1[0]*mat2[0])+(mat1[1]*mat2[2])) % b1, ((mat1[0]*mat2[1])+(mat1[1]*mat2[3])) % b1,
            ((mat1[2]*mat2[0])+(mat1[3]*mat2[2])) % b1, ((mat1[2]*mat2[1])+(mat1[3]*mat2[3])) % b1]
def fonk2(b3, b5):
    b2 = [1,1,1,0]
    while b5:
        if b5 & 1:
            b2 = fonk1(b2,b3)
        b3 = fonk1(b3, b3)
        b5 >>= 1
    return b2
def fonk3():
    b4 = input()
    while b4 > 0:
        f0,f1,b5 = map(int, raw_input().strip().split(' '))
        b3 = [1,1,1,0]
        b3 = fonk2(b3, b5-1)
        print ((b3[2]*f1)+(b3[3]*f0)) % ((10**9)+7)
        b4 -= 1
if b6 = = "__main__":
    fonk3()