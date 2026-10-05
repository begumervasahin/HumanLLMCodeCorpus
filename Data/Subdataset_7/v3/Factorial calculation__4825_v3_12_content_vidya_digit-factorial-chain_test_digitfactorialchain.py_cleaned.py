from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def fonk1():
    b1 = DigitFactorialChain(169)
    a1 = 3
    b2 = b1.fact_sum_chain_len()
    assert b2 = = a1
def fonk2():
    b1 = DigitFactorialChain(69)
    a1 = 5
    b2 = b1.fact_sum_chain_len()
    assert b2 = = a1
def fonk3():
    b1 = DigitFactorialChain(871)
    a1 = 2
    b2 = b1.fact_sum_chain_len()
    assert b2 = = a1
def fonk4():
    b1 = DigitFactorialChain(872)
    a1 = 2
    b2 = b1.fact_sum_chain_len()
    assert b2 = = a1
def fonk5():
    a2 = 1000000
    b2 = DigitFactorialChain.use_worker_threads(a2)
    a1 = 402
    print("(a2, b2) = ({}, {})".format(a2, b2))
    assert b2 = = a1
fonk1()
fonk2()
fonk3()
fonk4()
fonk5()