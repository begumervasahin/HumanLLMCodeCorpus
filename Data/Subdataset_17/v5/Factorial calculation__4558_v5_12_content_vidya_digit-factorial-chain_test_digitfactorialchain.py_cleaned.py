from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def test_basic_chain_length(n, expected_length):
    DigitFactorialChain.init_shared_area()
    dfc = DigitFactorialChain(n)
    result = dfc.fact_sum_chain_len()
    assert result == expected_length, f"Expected {expected_length}, got {result}"
def test_worker_threads(max_num, expected_result):
    result = DigitFactorialChain.use_worker_threads(max_num)
    print(f"(max_num, result) = ({max_num}, {result})")
    assert result == expected_result, f"Expected {expected_result}, got {result}"
def run_all_tests():
    test_basic_chain_length(169, 3)
    test_basic_chain_length(69, 5)
    test_basic_chain_length(871, 2)
    test_basic_chain_length(872, 2)
    test_worker_threads(1000000, 402)
    print("All tests passed.")
if __name__ == "__main__":
    run_all_tests()