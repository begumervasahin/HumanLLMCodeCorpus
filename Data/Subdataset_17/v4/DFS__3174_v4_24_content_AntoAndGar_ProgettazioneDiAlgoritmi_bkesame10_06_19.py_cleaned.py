def generate_combinations(length, index=0, current_combination=None):
    if current_combination is None:
        current_combination = []
    if index == length:
        print(''.join(current_combination))
        return
    for char in {'0', '1', '2', '3'}:
        if index == 0 or (char != str(int(current_combination[index - 1]) + 1) and char != str(int(current_combination[index - 1]) - 1)):
            current_combination.append(char)
            generate_combinations(length, index + 1, current_combination)
            current_combination.pop()
generate_combinations(6)