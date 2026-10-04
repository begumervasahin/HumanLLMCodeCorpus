from digitfactorialchain.digitfactorialchain import DigitFactorialChain
def fonk1(n, expected_length):
    DigitFactorialChain.init_shared_area()
    b1 = DigitFactorialChain(n)
    b2 = b1.fact_sum_chain_len()
    assert b2 = = expected_length, f"Expected {expected_length}, got {b2}"
def fonk2(max_num, expected_result):
    b2 = DigitFactorialChain.use_worker_threads(max_num)
    print(f"(max_num, b2) = ({max_num}, {b2})")
    assert b2 = = expected_result, f"Expected {expected_result}, got {b2}"
def fonk3():
    fonk1(169, 3)
    fonk1(69, 5)
    fonk1(871, 2)
    fonk1(872, 2)
    fonk2(1000000, 402)
    print("All tests passed.")
if b3 = = "__main__":
    fonk3()