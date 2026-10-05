from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def test_factorial_sum_chain_length_169():
    dfc = DigitFactorialChain(169)
    expected_length = 3
    result_length = dfc.fact_sum_chain_len()
    assert result_length == expected_length
def test_factorial_sum_chain_length_69():
    dfc = DigitFactorialChain(69)
    expected_length = 5
    result_length = dfc.fact_sum_chain_len()
    assert result_length == expected_length
def test_factorial_sum_chain_length_871():
    dfc = DigitFactorialChain(871)
    expected_length = 2
    result_length = dfc.fact_sum_chain_len()
    assert result_length == expected_length
def test_factorial_sum_chain_length_872():
    dfc = DigitFactorialChain(872)
    expected_length = 2
    result_length = dfc.fact_sum_chain_len()
    assert result_length == expected_length
def test_factorial_sum_chain_length_large_number():
    max_num = 1000000
    result_length = DigitFactorialChain.use_worker_threads(max_num)
    expected_length = 402
    print("(max_num, result_length) = ({}, {})".format(max_num, result_length))
    assert result_length == expected_length
test_factorial_sum_chain_length_169()
test_factorial_sum_chain_length_69()
test_factorial_sum_chain_length_871()
test_factorial_sum_chain_length_872()
test_factorial_sum_chain_length_large_number()