def find_combinations(candidates, target):
    candidates.sort()
    result_list = []
    current_combination = []
    _find_combinations_recursive(candidates, target, 0, current_combination, result_list)
    return result_list
def _find_combinations_recursive(candidates, target, start_index, current_combination, result_list):
    for i in range(start_index, len(candidates)):
        number = candidates[i]
        if number > target:
            break
        current_combination.append(number)
        if number < target:
            _find_combinations_recursive(candidates, target - number, i, current_combination, result_list)
        else:
            result_list.append(list(current_combination))
        current_combination.pop()
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = find_combinations(candidates, target)
    print("Unique combinations:", combinations)