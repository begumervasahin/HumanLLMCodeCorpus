def print_shanks_algorithm():
    MODULO = 2017
    BASE = 5
    MULTIPLIER = 1736
    RANGE_LIMIT = 46
    print("Shank's Algorithm!\n")
    print("S table:\n")
    s_values = {}
    for x in range(RANGE_LIMIT):
        s_value = (BASE**(45 * x)) % MODULO
        s_values[s_value] = x
        print(f"{x} {s_value}")
    print("\nT table:\n")
    t_values = []
    for y in range(RANGE_LIMIT):
        t_value = (MULTIPLIER * (BASE**y)) % MODULO
        t_values.append((y, t_value))
        print(f"{y} {t_value}")
    print("\nMatching Values:\n")
    for y, t_value in t_values:
        if t_value in s_values:
            x = s_values[t_value]
            print(f"{x} {y}")
print_shanks_algorithm()