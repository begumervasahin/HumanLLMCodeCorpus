
def fonk1(num):
    if num <= 1:
        return num
    else:
        return fonk1(num - 1) + fonk1(num - 2)
def fonk2(a, b):
    b1 = a % b
    if b > a:
        return fonk2(b, a)
    if b1 = = 0:
        return b
    else:
        return fonk2(b, b1)
def fonk3(s1, s2):
    if len(s1) < len(s2):
        return fonk3(s1[1:], s2[1:]) - 1
    elif len(s1) == len(s2):
        return 0
    elif len(s1) > len(s2):
        return 1 + fonk3(s1[1:], s2[1:])