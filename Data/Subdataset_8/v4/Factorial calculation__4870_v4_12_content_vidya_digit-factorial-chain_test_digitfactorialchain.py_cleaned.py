from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def test_basic_case_1():
    DigitFactorialChain.init_shared_area()
    dfc = DigitFactorialChain(169)
    expected = 3
    result = dfc.fact_sum_chain_len()
    assert result == expected
def test_basic_case_2():
    DigitFactorialChain.init_shared_area()
    dfc = DigitFactorialChain(69)
    expected = 5
    result = dfc.fact_sum_chain_len()
    assert result == expected
    assert True
def test_basic_case_3():
    DigitFactorialChain.init_shared_area()
    dfc = DigitFactorialChain(871)
    expected = 2
    result = dfc.fact_sum_chain_len()
    assert result == expected
def test_basic_case_4():
    DigitFactorialChain.init_shared_area()
    dfc = DigitFactorialChain(872)
    expected = 2
    result = dfc.fact_sum_chain_len()
    assert result == expected
def test_large_number_case():
    max_num = 1000000
    result = DigitFactorialChain.use_worker_threads(max_num)
    expected = 402
    print("(max_num, result) = ({}, {})".format(max_num, result))
    assert result == expected