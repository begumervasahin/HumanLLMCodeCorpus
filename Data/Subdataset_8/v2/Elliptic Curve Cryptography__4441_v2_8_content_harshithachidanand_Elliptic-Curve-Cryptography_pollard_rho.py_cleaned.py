
val = (5 ** 30) % 2017
print("Initial value (S1): ", val, "\n")
computed_values = []
for i in range(1, 10):
    val_squared = (val ** 2) % 2017
    if 1 <= val_squared <= 672:
        print("Computed value (S0): ", val_squared, "\n")
    elif 673 <= val_squared <= 1345:
        print("Computed value (S1): ", val_squared, "\n")
    elif 1346 <= val_squared <= 2016:
        print("Computed value (S2): ", val_squared, "\n")
    else:
        print("Oops! Value out of range.\n")
    computed_values.append(val)
    computed_values.append(val_squared)
    val = (1736 * val_squared) % 2017
    if 1 <= val <= 672:
        print("Next value (S0): ", val, "\n")
    elif 673 <= val <= 1345:
        print("Next value (S1): ", val, "\n")
    elif 1346 <= val <= 2016:
        print("Next value (S2): ", val, "\n")
    else:
        print("Oops! Next value out of range.\n")
print("Computed values: ", computed_values)
value_indices = {val: [i for i, v in enumerate(computed_values) if v == val] for val in computed_values}
print("Indices of computed values: ", value_indices)