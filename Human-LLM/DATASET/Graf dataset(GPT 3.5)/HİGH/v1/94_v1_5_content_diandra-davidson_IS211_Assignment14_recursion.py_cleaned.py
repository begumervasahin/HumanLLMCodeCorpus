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
def fonk4():
    assert fonk1(0) == 0
    assert fonk1(1) == 1
    assert fonk1(2) == 1
    assert fonk1(3) == 2
    assert fonk1(4) == 3
def fonk5():
    assert fonk2(48, 18) == 6
    assert fonk2(60, 48) == 12
    assert fonk2(21, 14) == 7
    assert fonk2(17, 5) == 1
def fonk6():
    assert fonk3("hello", "world") == -3
    assert fonk3("hello", "hi") == 2
    assert fonk3("hello", "hello") == 0
if b2 = = "__main__":
    fonk4()
    fonk5()
    fonk6()
    print("All tests passed!")