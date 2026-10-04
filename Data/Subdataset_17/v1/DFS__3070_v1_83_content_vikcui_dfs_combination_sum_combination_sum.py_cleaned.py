def combination_sum_aux(candidates, target):
    candidates.sort()
    result_list = []
    result_seq = []
    combination_sum(candidates, target, 0, result_seq, result_list)
    return result_list
def combination_sum(candidates, target, current_index, result_seq, result_list):
    for j in range(current_index, len(candidates)):
        num = candidates[j]
        if num > target:
            break
        result_seq.append(num)
        if num < target:
            combination_sum(candidates, target - num, j, result_seq, result_list)
        else:
            result_list.append(list(result_seq))
        result_seq.pop()
if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    combinations = combination_sum_aux(candidates, target)
    print("Unique combinations:", combinations)