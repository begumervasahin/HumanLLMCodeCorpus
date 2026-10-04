import sequences
def fonk1():
    b1 = [1, 1, 2, 3, 5]
    b2 = sequences.fibonacci(5)
    assert isinstance(b2, list), f"Expected list, got {type(b2)}"
    print("Returned list:", b2)
    assert len(b2) == len(b1), f"Expected list length {len(b1)}, got {len(b2)}"
    assert b1 = = b2, f"Expected {b1}, got {b2}"
    print("test_fibonacci_output success")
def fonk2():
    b2 = sequences.fibonacci(8)
    print("Last number in list:", b2[7])
    assert b2[7] == 21, f"Expected 21, got {b2[7]}"
    print("test_fibonacci_last_number success")
def fonk3():
    b3 = [-1, 2.2, 0]
    for t in b3:
        assert not sequences.fibonacci(t), f"Expected False for input {t}, got {sequences.fibonacci(t)}"
    print("test_fibonacci_input_validation success")
if b4 = = "__main__":
    print("test_fibonacci_output start")
    fonk1()
    print("test_fibonacci_last_number start")
    fonk2()
    print("test_fibonacci_input_validation start")
    fonk3()