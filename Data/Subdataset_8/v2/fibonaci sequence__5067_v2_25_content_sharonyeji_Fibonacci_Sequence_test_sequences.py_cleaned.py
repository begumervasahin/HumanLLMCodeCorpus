import sequences
def test_return_value_matches_expected_result():
    expected_list = [1, 1, 2, 3, 5]
    ret_list = sequences.fibonacci(5)
    assert isinstance(ret_list, list)
    assert len(ret_list) == len(expected_list)
    assert expected_list == ret_list
    print("Test 1 success")
def test_last_number_of_fibonacci_list():
    ret_list = sequences.fibonacci(8)
    print(ret_list[7])
    assert ret_list[7] == 21
    print("Test 2 success")
def test_input_validation():
    invalid_values = [-1, 2.2, 0]
    for value in invalid_values:
        assert not sequences.fibonacci(value)
    print("Input validation success")
if __name__ == "__main__":
    print("Test 1 start")
    test_return_value_matches_expected_result()
    print("Test 2 start")
    test_last_number_of_fibonacci_list()
    print("Test 3 start")
    test_input_validation()