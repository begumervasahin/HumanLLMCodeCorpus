
val = (5**30) % 2017
print(f"S1 {val}\n")
values = []
for _ in range(1, 10):
    val2 = (val**2) % 2017
    if 1 <= val2 <= 672:
        print(f"S0 {val2}\n")
    elif 673 <= val2 <= 1345:
        print(f"S1 {val2}\n")
    elif 1346 <= val2 <= 2016:
        print(f"S2 {val2}\n")
    else:
        print("oops\n")
    values.append(val)
    values.append(val2)
    val = (1736 * val2) % 2017
    if 1 <= val <= 672:
        print(f"S0 {val}\n")
    elif 673 <= val <= 1345:
        print(f"S1 {val}\n")
    elif 1346 <= val <= 2016:
        print(f"S2 {val}\n")
    else:
        print("oops\n")
print(values)
value_indices = {}
for i, value in enumerate(values):
    if value not in value_indices:
        value_indices[value] = []
    value_indices[value].append(i)
print(value_indices)