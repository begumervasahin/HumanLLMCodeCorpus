def generate_prime_numbers(n):
    if n is None:
        print("Please enter a positive integer as the limit!")
        return "Please enter a positive integer as the limit!"
    if not isinstance(n, int):
        print("That is not an integer. Please enter a number without a decimal")
        return "That is not an integer. Please enter a number without a decimal"
    if n <= 0:
        print("Please enter a positive integer")
        return "Please enter a positive integer"
    print("Hello")
    if n == 0:
        return [0]
    elif n == 2:
        return [2]
    prime_numbers = []
    s = list(range(3, n + 1, 2))
    mroot = int(n ** 0.5)
    half = (n + 1)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]