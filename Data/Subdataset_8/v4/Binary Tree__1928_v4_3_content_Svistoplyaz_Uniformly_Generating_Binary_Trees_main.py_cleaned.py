from collections import namedtuple
import random
import bisect
TreeNode = namedtuple("TreeNode", "value left_child right_child")
catalan_numbers = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
                   35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650,
                   1289904147324, 4861946401452]
max_n = len(catalan_numbers) - 1
average_max_height = [-1] * (max_n + 1)
prob_distr = [{} for _ in range(max_n + 1)]
average_leaves = [-1] * (max_n + 1)
prob_distr_leaves = [{} for _ in range(max_n + 1)]
average_height = [-1] * (max_n + 1)
prob_distr_av_height = [{} for _ in range(max_n + 1)]
cur_value = 0
def generate_binary_tree(n):
    global cur_value
    if n == 0 or n > max_n:
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
    if n > max_n:
        return None
    if average_max_height[n] != -1:
        return average_max_height[n]
    sum_height = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_height += coef * max(compute_average_max_height(i), compute_average_max_height(n - 1 - i))
    average_max_height[n] = 1 + sum_height / coef_sum
    return average_max_height[n]
def compute_prob_distr_max_height(n):
    if n > max_n:
        return None
    if prob_distr[n] != {}:
        return prob_distr[n]
    for i in range(n):
        left_distr = compute_prob_distr_max_height(i)
        right_distr = compute_prob_distr_max_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr.keys():
            for right_key in right_distr.keys():
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = 1 + max(left_key, right_key)
                what_to_write = left_prob * right_prob * coef
                if write_to_key in prob_distr[n]:
                    prob_distr[n][write_to_key] += what_to_write
                else:
                    prob_distr[n][write_to_key] = what_to_write
    return prob_distr[n]
def compute_average_leaves(n):
    if n > max_n:
        return None
    if average_leaves[n] != -1:
        return average_leaves[n]
    sum_leaves = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_leaves += coef * (compute_average_leaves(i) + compute_average_leaves(n - 1 - i))
    average_leaves[n] = sum_leaves / coef_sum
    return average_leaves[n]
def compute_prob_distr_leaves(n):
    if n > max_n:
        return None
    if prob_distr_leaves[n] != {}:
        return prob_distr_leaves[n]
    for i in range(n):
        left_distr = compute_prob_distr_leaves(i)
        right_distr = compute_prob_distr_leaves(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr.keys():
            for right_key in right_distr.keys():
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = left_key + right_key
                what_to_write = left_prob * right_prob * coef
                if write_to_key in prob_distr_leaves[n]:
                    prob_distr_leaves[n][write_to_key] += what_to_write
                else:
                    prob_distr_leaves[n][write_to_key] = what_to_write
    return prob_distr_leaves[n]
def compute_average_height(n):
    if n > max_n:
        return None
    if average_height[n] != -1:
        return average_height[n]
    sum_height = 0
    coef_sum = 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        sum_height += coef * ((n - 1) + compute_average_height(i) + compute_average_height(n - 1 - i))
    average_height[n] = sum_height / coef_sum
    return average_height[n]
def compute_prob_distr_av_height(n):
    if n > max_n:
        return None
    if prob_distr_av_height[n] != {}:
        return prob_distr_av_height[n]
    for i in range(n):
        left_distr = compute_prob_distr_av_height(i)
        right_distr = compute_prob_distr_av_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr.keys():
            for right_key in right_distr.keys():
                left_prob = left_distr[left_key]
                right_prob = right_distr[right_key]
                write_to_key = left_key + right_key + n - 1
                what_to_write = left_prob * right_prob * coef
                if write_to_key in prob_distr_av_height[n]:
                    prob_distr_av_height[n][write_to_key] += what_to_write
                else:
                    prob_distr_av_height[n][write_to_key] = what_to_write
    return prob_distr_av_height[n]
def sub_func_average_height(n):
    return compute_average_height(n) / n
def sub_function_distr_av_height(n):
    dict = compute_prob_distr_av_height(n)
    res_dict = {}
    for key in dict.keys():
        res_dict[key/n] = dict[key]
    return res_dict
if __name__ == "__main__":
    tree_root = generate_binary_tree(5)
    print(str(sub_func_average_height(3)))
    print(str(sub_function_distr_av_height(3)))