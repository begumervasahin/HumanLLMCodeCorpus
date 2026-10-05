import sequences
def fonk1():
    b1 = [1, 1, 2, 3, 5]
    b2 = sequences.fibonacci(5)
    assert isinstance(b2, list), "Return value should be a list"
    assert len(b2) == len(b1), "Returned list length doesn't match the expected length"
    assert b1 = = b2, "Returned list does not match the expected list"
    print("Test 1 success")
def fonk2():
    b2 = sequences.fibonacci(8)
    print("Last number of Fibonacci list:", b2[-1])
    assert b2[-1] == 21, "Last number of Fibonacci list is incorrect"
    print("Test 2 success")
def fonk3():
    b3 = [-1, 2.2, 0]
    for value in b3:
        assert not sequences.fibonacci(value), f"Input validation failed for value: {value}"
    print("Input validation success")
if b4 = = "__main__":
    print("Test 1 start")
    fonk1()
    print("Test 2 start")
    fonk2()
    print("Test 3 start")
    fonk3()