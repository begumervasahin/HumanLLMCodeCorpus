import sequences
def fonk1():
    b1 = [1,1,2,3,5]
    b2 = sequences.fibonacci(5)
    assert type(b2) == list
    print(b2)
    assert len(b2) == len(b1)
    assert b1 = = b2
    print("test1 success")
    return
def fonk2():
    b2 = sequences.fibonacci(8)
    print(b2[7])
    assert b2[7] == 21
    print("test2 success")
    return
def fonk3():
    a1 = -1
    assert sequences.fibonacci(a1) == False
    a1 = 2.2
    assert sequences.fibonacci(a1) == False
    a1 = 0
    assert sequences.fibonacci(a1) == False
    print("input validation success")
    return
print("test1-start")
fonk1()
print("test2 start")
fonk2()
print("test3 start")
fonk3()