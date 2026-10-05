
initial_value = (5 ** 30) % 2017
print("Initial value (S1):", initial_value, "\n")
values_list = []
for iteration in range(1, 10):
    squared_value = (initial_value ** 2) % 2017
    if 1 <= squared_value <= 672:
        category = "S0"
    elif 673 <= squared_value <= 1345:
        category = "S1"
    elif 1346 <= squared_value <= 2016:
        category = "S2"
    else:
        category = "Oops"
    print(f"{category}: {squared_value}\n")
    values_list.append(initial_value)
    values_list.append(squared_value)
    next_value = (1736 * squared_value) % 2017
    if 1 <= next_value <= 672:
        next_category = "S0"
    elif 673 <= next_value <= 1345:
        next_category = "S1"
    elif 1346 <= next_value <= 2016:
        next_category = "S2"
    else:
        next_category = "Oops"
    print(f"{next_category}: {next_value}\n")
    initial_value = next_value
print("Values list:", values_list)
mapped_values = {value: [index for index, val in enumerate(values_list) if val == value] for value in values_list}
print("Mapped values:", mapped_values)