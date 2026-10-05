import sequences
def test_return_value_matches_expected_result():
    expected_sequence = [1, 1, 2, 3, 5]
    returned_sequence = sequences.fibonacci(5)
    assert isinstance(returned_sequence, list), "Return value should be a list"
    assert len(returned_sequence) == len(expected_sequence), "Returned list length doesn't match the expected length"
    assert expected_sequence == returned_sequence, "Returned list does not match the expected list"
    print("Test 1 success")
def test_last_number_of_fibonacci_list():
    fibonacci_sequence = sequences.fibonacci(8)
    last_number = fibonacci_sequence[-1]
    print("Last number of Fibonacci sequence:", last_number)
    assert last_number == 21, "Last number of Fibonacci sequence is incorrect"
    print("Test 2 success")
def test_input_validation():
    invalid_values = [-1, 2.2, 0]
    for value in invalid_values:
        assert not sequences.fibonacci(value), f"Input validation failed for value: {value}"
    print("Input validation success")
if __name__ == "__main__":
    print("Test 1 start")
    test_return_value_matches_expected_result()
    print("Test 2 start")
    test_last_number_of_fibonacci_list()
    print("Test 3 start")
    test_input_validation()