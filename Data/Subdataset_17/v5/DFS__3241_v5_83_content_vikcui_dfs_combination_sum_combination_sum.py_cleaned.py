def combination_sum(candidates, target):
    candidates.sort()
    result_list = []
    _find_combinations(candidates, target, 0, [], result_list)
    return result_list
def _find_combinations(candidates, target, start_index, current_combination, result_list):
    for i in range(start_index, len(candidates)):
        num = candidates[i]
        if num > target:
            break
        current_combination.append(num)
        if num < target:
            _find_combinations(candidates, target - num, i, current_combination, result_list)
        else:
            result_list.append(list(current_combination))
        current_combination.pop()
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = combination_sum(candidates, target)
    print("Unique combinations:", combinations)