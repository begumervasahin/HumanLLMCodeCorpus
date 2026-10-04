def generate_combinations(length, index=0, current_combination=None):
    if current_combination is None:
        current_combination = []
    if index == length:
        print(''.join(current_combination))
        return
    for char in {'0', '1', '2', '3'}:
        if is_valid_char(current_combination, index, char):
            current_combination.append(char)
            generate_combinations(length, index + 1, current_combination)
            current_combination.pop()
def is_valid_char(current_combination, index, char):
    if index == 0:
        return True
    previous_char = current_combination[index - 1]
    return char != str(int(previous_char) + 1) and char != str(int(previous_char) - 1)
generate_combinations(6)