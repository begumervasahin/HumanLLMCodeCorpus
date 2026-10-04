from collections import namedtuple
import random
import bisect
TreeNode = namedtuple("TreeNode", ["value", "left_child", "right_child"])
catalan_numbers = [
    1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845,
    35357670, 129644790, 477638700, 1767263190, 6564120420, 24466267020, 91482563640, 343059613650,
    1289904147324, 4861946401452
]
max_n = len(catalan_numbers) - 1
average_max_height = [-1] * (max_n + 1)
average_max_height[0] = average_max_height[1] = 0
prob_distr = [{} for _ in range(max_n + 1)]
prob_distr[0] = {0: 1}
prob_distr[1] = {0: 1}
average_leaves = [-1] * (max_n + 1)
average_leaves[0] = 0
average_leaves[1] = 1
prob_distr_leaves = [{} for _ in range(max_n + 1)]
prob_distr_leaves[0] = {0: 1}
prob_distr_leaves[1] = {1: 1}
average_height = [-1] * (max_n + 1)
average_height[0] = average_height[1] = 0
prob_distr_av_height = [{} for _ in range(max_n + 1)]
prob_distr_av_height[0] = {0: 1}
prob_distr_av_height[1] = {0: 1}
cur_value = 0
def generate_binary_tree(n):
    global cur_value
    if n == 0 or n > max_n:
        return None
    root = TreeNode(value=cur_value, left_child=None, right_child=None)
    cur_value += 1
    if n == 1:
        return root
    chances = [catalan_numbers[0] * catalan_numbers[n - 1]]
    for i in range(1, n):
        chances.append(chances[i - 1] + catalan_numbers[i] * catalan_numbers[n - 1 - i])
    max_chance = chances[-1]
    chosen_chance = random.randint(1, max_chance)
    index = bisect.bisect_left(chances, chosen_chance)
    root = root._replace(left_child=generate_binary_tree(index))
    root = root._replace(right_child=generate_binary_tree(n - 1 - index))
    return root
def compute_average_max_height(n):
    if n > max_n:
        return None
    if average_max_height[n] != -1:
        return average_max_height[n]
    total, coef_sum = 0, 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        total += coef * max(compute_average_max_height(i), compute_average_max_height(n - 1 - i))
    average_max_height[n] = 1 + total / coef_sum
    return average_max_height[n]
def compute_prob_distr_max_height(n):
    if n > max_n:
        return None
    if prob_distr[n]:
        return prob_distr[n]
    for i in range(n):
        left_distr = compute_prob_distr_max_height(i)
        right_distr = compute_prob_distr_max_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                key = 1 + max(left_key, right_key)
                prob_distr[n][key] = prob_distr[n].get(key, 0) + left_distr[left_key] * right_distr[right_key] * coef
    return prob_distr[n]
def compute_average_leaves(n):
    if n > max_n:
        return None
    if average_leaves[n] != -1:
        return average_leaves[n]
    total, coef_sum = 0, 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        total += coef * (compute_average_leaves(i) + compute_average_leaves(n - 1 - i))
    average_leaves[n] = total / coef_sum
    return average_leaves[n]
def compute_prob_distr_leaves(n):
    if n > max_n:
        return None
    if prob_distr_leaves[n]:
        return prob_distr_leaves[n]
    for i in range(n):
        left_distr = compute_prob_distr_leaves(i)
        right_distr = compute_prob_distr_leaves(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                key = left_key + right_key
                prob_distr_leaves[n][key] = prob_distr_leaves[n].get(key, 0) + left_distr[left_key] * right_distr[right_key] * coef
    return prob_distr_leaves[n]
def compute_average_height(n):
    if n > max_n:
        return None
    if average_height[n] != -1:
        return average_height[n]
    total, coef_sum = 0, 0
    for i in range(n):
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i]
        coef_sum += coef
        total += coef * ((n - 1) + compute_average_height(i) + compute_average_height(n - 1 - i))
    average_height[n] = total / coef_sum
    return average_height[n]
def compute_prob_distr_av_height(n):
    if n > max_n:
        return None
    if prob_distr_av_height[n]:
        return prob_distr_av_height[n]
    for i in range(n):
        left_distr = compute_prob_distr_av_height(i)
        right_distr = compute_prob_distr_av_height(n - 1 - i)
        coef = catalan_numbers[i] * catalan_numbers[n - 1 - i] / catalan_numbers[n]
        for left_key in left_distr:
            for right_key in right_distr:
                key = left_key + right_key + n - 1
                prob_distr_av_height[n][key] = prob_distr_av_height[n].get(key, 0) + left_distr[left_key] * right_distr[right_key] * coef
    return prob_distr_av_height[n]
def average_height_per_node(n):
    return compute_average_height(n) / n
def prob_distr_av_height_per_node(n):
    distribution = compute_prob_distr_av_height(n)
    return {key / n: value for key, value in distribution.items()}
if __name__ == "__main__":
    tree_root = generate_binary_tree(5)
    print("Average height per node for n=3:", average_height_per_node(3))
    print("Probability distribution of average height per node for n=3:", prob_distr_av_height_per_node(3))