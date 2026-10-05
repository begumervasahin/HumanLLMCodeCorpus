from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def test_basic_cases():
    dfc_169 = DigitFactorialChain(169)
    expected_169 = 3
    result_169 = dfc_169.fact_sum_chain_len()
    assert result_169 == expected_169
    dfc_69 = DigitFactorialChain(69)
    expected_69 = 5
    result_69 = dfc_69.fact_sum_chain_len()
    assert result_69 == expected_69
    dfc_871 = DigitFactorialChain(871)
    expected_871 = 2
    result_871 = dfc_871.fact_sum_chain_len()
    assert result_871 == expected_871
    dfc_872 = DigitFactorialChain(872)
    expected_872 = 2
    result_872 = dfc_872.fact_sum_chain_len()
    assert result_872 == expected_872
def test_large_number_case():
    max_num = 1000000
    result = DigitFactorialChain.use_worker_threads(max_num)
    expected = 402
    print("(max_num, result) = ({}, {})".format(max_num, result))
    assert result == expected