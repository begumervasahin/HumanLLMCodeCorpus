def pd_sequence(n):
    T = [0] * (n + 1)
    T[0] = 1
    T[1] = 4
    T[2] = 10
    for i in range(3, n + 1):
        T[i] = 3 * T[i - 1] - T[i - 2]
    return T[n]
if __name__ == "__main__":
    n = 5
    result = pd_sequence(n)
    print(f"The {n}th value in the sequence is: {result}")