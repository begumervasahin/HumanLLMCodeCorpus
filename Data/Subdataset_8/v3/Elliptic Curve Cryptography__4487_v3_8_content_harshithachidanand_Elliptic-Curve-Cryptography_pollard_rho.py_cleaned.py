
initial_value = (5 ** 30) % 2017
print("Initial value (S1): ", initial_value, "\n")
computed_values = []
for i in range(1, 10):
    squared_value = (initial_value ** 2) % 2017
    if 1 <= squared_value <= 672:
        category = "S0"
    elif 673 <= squared_value <= 1345:
        category = "S1"
    elif 1346 <= squared_value <= 2016:
        category = "S2"
    else:
        category = "Oops! Value out of range."
    print(f"Computed value ({category}): {squared_value}\n")
    computed_values.append(initial_value)
    computed_values.append(squared_value)
    next_value = (1736 * squared_value) % 2017
    if 1 <= next_value <= 672:
        next_category = "S0"
    elif 673 <= next_value <= 1345:
        next_category = "S1"
    elif 1346 <= next_value <= 2016:
        next_category = "S2"
    else:
        next_category = "Oops! Next value out of range."
    print(f"Next value ({next_category}): {next_value}\n")
    initial_value = next_value
print("Computed values:", computed_values)
value_indices = {val: [i for i, v in enumerate(computed_values) if v == val] for val in computed_values}
print("Indices of computed values:", value_indices)