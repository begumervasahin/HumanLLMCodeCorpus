def calculate_golden_ratio(n):
    golden_ratios = []
    s, t = 1, 1
    for _ in range(2, n):
        c = s + t
        s, t = t, c
        ratio = t / s
        golden_ratios.append(ratio)
    return golden_ratios
def print_golden_ratio(n):
    golden_ratios = calculate_golden_ratio(n)
    for ratio in golden_ratios:
        print(ratio)
if __name__ == "__main__":
    print_golden_ratio(1476)