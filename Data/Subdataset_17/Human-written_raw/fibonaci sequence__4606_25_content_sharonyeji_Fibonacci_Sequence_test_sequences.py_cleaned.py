import sequences
def test1():
    expectedList=[1,1,2,3,5]
    retList=sequences.fibonacci(5)
    assert type(retList) == list
    print(retList)
    assert len(retList) == len(expectedList)
    assert expectedList == retList
    print("test1 success")
    return
def test2():
    retList = sequences.fibonacci(8)
    print(retList[7])
    assert retList[7] == 21
    print("test2 success")
    return
def test3():
    t=-1
    assert sequences.fibonacci(t) == False
    t=2.2
    assert sequences.fibonacci(t) == False
    t=0
    assert sequences.fibonacci(t) == False
    print("input validation success")
    return
print("test1-start")
test1()
print("test2 start")
test2()
print("test3 start")
test3()