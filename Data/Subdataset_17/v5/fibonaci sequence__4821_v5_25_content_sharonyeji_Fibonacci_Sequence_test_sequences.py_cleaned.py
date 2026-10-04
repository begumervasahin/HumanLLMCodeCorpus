import sequences
def test_fibonacci_output():
    expected_list = [1, 1, 2, 3, 5]
    ret_list = sequences.fibonacci(5)
    assert isinstance(ret_list, list), f"Expected list, got {type(ret_list)}"
    assert len(ret_list) == len(expected_list), f"Expected list length {len(expected_list)}, got {len(ret_list)}"
    assert expected_list == ret_list, f"Expected {expected_list}, got {ret_list}"
    print("Returned list:", ret_list)
    print("test_fibonacci_output success")
def test_fibonacci_last_number():
    ret_list = sequences.fibonacci(8)
    assert len(ret_list) > 7, f"Expected list length greater than 7, got {len(ret_list)}"
    assert ret_list[7] == 21, f"Expected 21, got {ret_list[7]}"
    print("Last number in list:", ret_list[7])
    print("test_fibonacci_last_number success")
def test_fibonacci_input_validation():
    invalid_inputs = [-1, 2.2, 0]
    for t in invalid_inputs:
        assert not sequences.fibonacci(t), f"Expected False for input {t}, got {sequences.fibonacci(t)}"
    print("test_fibonacci_input_validation success")
if __name__ == "__main__":
    print("Starting test_fibonacci_output")
    test_fibonacci_output()
    print("Starting test_fibonacci_last_number")
    test_fibonacci_last_number()
    print("Starting test_fibonacci_input_validation")
    test_fibonacci_input_validation()