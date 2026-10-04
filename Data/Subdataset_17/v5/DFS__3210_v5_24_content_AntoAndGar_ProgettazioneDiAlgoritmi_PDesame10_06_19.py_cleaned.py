def pd_sequence(n):
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    T = [0] * (n + 1)
    base_cases = {0: 1, 1: 4, 2: 10}
    for i in range(min(3, n + 1)):
        T[i] = base_cases[i]
    for i in range(3, n + 1):
        T[i] = 3 * T[i - 1] - T[i - 2]
    return T[n]
if __name__ == "__main__":
    n = 5
    result = pd_sequence(n)
    print(f"The {n}th value in the sequence is: {result}")