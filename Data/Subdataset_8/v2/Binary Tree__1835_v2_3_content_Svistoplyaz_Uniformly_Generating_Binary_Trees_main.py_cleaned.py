from collections import namedtuple
import random
import bisect
TreeNode = namedtuple("TreeNode", "value left_child right_child")
catalan_numbers = [
    1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440,
    9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020,
    91482563640, 343059613650, 1289904147324, 4861946401452
]
MAX_N = len(catalan_numbers) - 1
average_max_height = [0, 0] + [-1] * MAX_N
prob_distr = [{0: 1}, {0: 1}] + [{} for _ in range(MAX_N)]
average_leaves = [0, 1] + [-1] * MAX_N
prob_distr_leaves = [{0: 1}, {1: 1}] + [{} for _ in range(MAX_N)]
average_height = [0, 0] + [-1] * MAX_N
prob_distr_av_height = [{0: 1}, {0: 1}] + [{} for _ in range(MAX_N)]
cur_value = 0
def generate_binary_tree(n):
    global cur_value
    if n == 0 or n > MAX_N:
        return None
    root = TreeNode(value=cur_value, left_child=None, right_child=None)
    cur_value += 1
    if n == 1:
        return root
    chance = [catalan_numbers[0] * catalan_numbers[n - 1]]
    for i in range(1, n):
        chance.append(chance[i - 1] + catalan_numbers[i] * catalan_numbers[n - 1 - i])
    max_number = chance[n - 1]
    chosen_chance = random.randint(1, max_number)
    index = bisect.bisect_left(chance, chosen_chance)
    root = root._replace(left_child=generate_binary_tree(index))
    root = root._replace(right_child=generate_binary_tree(n - 1 - index))
    return root
def compute_average_max_height(n):
    if n > MAX_N:
        return None
    if average_max_height[n] != -1:
        return average_max_height[n]
    sum_val = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_val += coef * max(compute_average_max_height(i), compute_average_max_height(n - 1 - i))
    ans = 1 + sum_val / coef_sum
    average_max_height[n] = ans
    return ans
def compute_prob_distr_max_height(n):
    if n > MAX_N:
        return None
    if prob_distr[n]:
        return prob_distr[n]
    for i in range(n):
        left_distr = compute_prob_distr_max_height(i)
        right_distr = compute_prob_distr_max_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = 1 + max(left_key, right_key)
                what_to_write = left_prob * right_prob * coef
                prob_distr[n][write_to_key] = prob_distr[n].get(write_to_key, 0) + what_to_write
    return prob_distr[n]
def compute_average_leaves(n):
    if n > MAX_N:
        return None
    if average_leaves[n] != -1:
        return average_leaves[n]
    sum_val = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_val += coef * (compute_average_leaves(i) + compute_average_leaves(n - 1 - i))
    ans = sum_val / coef_sum
    average_leaves[n] = ans
    return ans
def compute_prob_distr_leaves(n):
    if n > MAX_N:
        return None
    if prob_distr_leaves[n]:
        return prob_distr_leaves[n]
    for i in range(n):
        left_distr = compute_prob_distr_leaves(i)
        right_distr = compute_prob_distr_leaves(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = left_key + right_key
                what_to_write = left_prob * right_prob * coef
                prob_distr_leaves[n][write_to_key] = prob_distr_leaves[n].get(write_to_key, 0) + what_to_write
    return prob_distr_leaves[n]
def sub_func_average_height(n):
    return compute_average_height(n) / n
def compute_average_height(n):
    if n > MAX_N:
        return None
    if average_height[n] != -1:
        return average_height[n]
    sum_val = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_val += coef * ((n - 1) + compute_average_height(i) + compute_average_height(n - 1 - i))
    ans = sum_val / coef_sum
    average_height[n] = ans
    return ans
def sub_function_distr_av_height(n):
    dict_val = compute_prob_distr_av_height(n)
    res_dict = {}
    for key in dict_val:
        res_dict[key/n] = dict_val[key]
    return res_dict
def compute_prob_distr_av_height(n):
    if n > MAX_N:
        return None
    if prob_distr_av_height[n]:
        return prob_distr_av_height[n]
    for i in range(n):
        left_distr = compute_prob_distr_av_height(i)
        right_distr = compute_prob_distr_av_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = left_key + right_key + n - 1
                what_to_write = left_prob * right_prob * coef
                prob_distr_av_height[n][write_to_key] = prob_distr_av_height[n].get(write_to_key, 0) + what_to_write
    return prob_distr_av_height[n]
if __name__ == "__main__":
    tree_root = generate_binary_tree(5)
    print(str(sub_func_average_height(3)))
    print(str(sub_function_distr_av_height(3)))