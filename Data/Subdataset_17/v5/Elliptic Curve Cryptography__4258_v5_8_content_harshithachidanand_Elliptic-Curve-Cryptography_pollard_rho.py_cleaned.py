def classify_value(val):
    if 1 <= val <= 672:
        return f"S0 {val}\n"
    elif 673 <= val <= 1345:
        return f"S1 {val}\n"
    elif 1346 <= val <= 2016:
        return f"S2 {val}\n"
    else:
        return "oops\n"
def main():
    val = (5**30) % 2017
    print(f"S1 {val}\n")
    values = []
    for _ in range(1, 10):
        val2 = (val**2) % 2017
        print(classify_value(val2))
        values.extend([val, val2])
        val = (1736 * val2) % 2017
        print(classify_value(val))
    print(values)
    value_indices = {}
    for index, value in enumerate(values):
        if value not in value_indices:
            value_indices[value] = []
        value_indices[value].append(index)
    print(value_indices)
if __name__ == "__main__":
    main()