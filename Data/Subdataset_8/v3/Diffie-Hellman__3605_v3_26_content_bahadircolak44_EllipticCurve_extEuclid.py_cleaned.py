import time
def extended_gcd(a, b):
    current_remainder = -1
    original_b = b
    original_a = a
    equation_set = []
    full_equation_set = []
    modular_set = []
    while current_remainder != 1 and current_remainder != 0:
        current_remainder = b % a
        quotient = b
        equation_set = [current_remainder, b, a, quotient * -1]
        b = a
        a = current_remainder
        full_equation_set.append(equation_set)
    for i in range(0, 4):
        modular_set.append(full_equation_set[-1][i])
    modular_set.insert(2, 1)
    counter = 0
    for i in range(1, len(full_equation_set)):
        if counter % 2 == 0:
            modular_set[2] = full_equation_set[-1 * (i + 1)][3] * modular_set[4] + modular_set[2]
            modular_set[3] = full_equation_set[-1 * (i + 1)][1]
        elif counter % 2 != 0:
            modular_set[4] = full_equation_set[-1 * (i + 1)][3] * modular_set[2] + modular_set[4]
            modular_set[1] = full_equation_set[-1 * (i + 1)][1]
        counter += 1
    if modular_set[3] == original_b:
        return modular_set[2] % original_b
    return modular_set[4] % original_b
start_time = time.time()
result = extended_gcd(1436354634563546363456435635634564572437693486572348678234768374623,
                      123231461346134613746783174587319485798317589721387645783465763174567163457617346578136475863441)
end_time = time.time()
print("Extended GCD Result:", result)
print("Execution time: %.2f seconds" % (end_time - start_time))