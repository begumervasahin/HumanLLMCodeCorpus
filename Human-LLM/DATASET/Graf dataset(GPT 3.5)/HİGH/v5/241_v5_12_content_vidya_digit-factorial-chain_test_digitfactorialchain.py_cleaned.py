from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def fonk1():
    b1 = DigitFactorialChain(169)
    a1 = 3
    b2 = b1.fact_sum_chain_len()
    assert b2 = = a1
    b3 = DigitFactorialChain(69)
    a2 = 5
    b4 = b3.fact_sum_chain_len()
    assert b4 = = a2
    b5 = DigitFactorialChain(871)
    a3 = 2
    b6 = b5.fact_sum_chain_len()
    assert b6 = = a3
    b7 = DigitFactorialChain(872)
    a4 = 2
    b8 = b7.fact_sum_chain_len()
    assert b8 = = a4
def fonk2():
    a5 = 1000000
    b9 = DigitFactorialChain.use_worker_threads(a5)
    a6 = 402
    print("(a5, b9) = ({}, {})".format(a5, b9))
    assert b9 = = a6