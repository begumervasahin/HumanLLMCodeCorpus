def list_to_string(char_list):
    return ''.join(char_list)
def print_numbers_up_to(n):
    if n >= 1:
        print_numbers_up_to(n - 1)
        print(str(n))
    else:
        return
def print_numbers_down_to(n):
    if n >= 1:
        print(str(n))
        print_numbers_down_to(n - 1)
def has_divisor_smaller_than(n, i):
    if i == 1 or i == 0:
        return False
    elif n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)
def is_prime(n):
    if n < 2:
        return False
    i = int(n ** 0.5)
    if not has_divisor_smaller_than(n, i):
        return True
    return False
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
def exponential_limit(n, x):
    if n == 0:
        return 1
    return (x ** n) / factorial(n) + exponential_limit(n - 1, x)
def solve_hanoi_towers(hanoi, n, src, dest, temp):
    if n < 1:
        return
    elif n == 1:
        hanoi.move(src, dest)
        return
    solve_hanoi_towers(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    solve_hanoi_towers(hanoi, n - 1, temp, dest, src)
def print_all_sequences(char_list, n):
    if n == 0:
        return
    k = n
    n = len(set(char_list))
    print_sequences_recursive(char_list, "", n, k)
def print_sequences_recursive(char_list, prefix, n, k):
    if k == 0:
        print(prefix)
        return
    for i in range(n):
        new_prefix = prefix + char_list[i]
        print_sequences_recursive(char_list, new_prefix, n, k - 1)
def print_unique_sequences(char_list, n):
    if n == 0:
        return
    print_no_repetition_sequences_recursive(char_list, "", n)
def print_no_repetition_sequences_recursive(char_list, prefix, n):
    if n == 0:
        print(prefix)
        return
    for i, char in enumerate(char_list):
        new_prefix = prefix + char
        print_no_repetition_sequences_recursive(char_list[:i] + char_list[i+1:], new_prefix, n - 1)
def generate_parentheses(n):
    str_lst = [""] * 2 * n
    results_lst = []
    if n > 0:
        generate_parentheses_recursive(str_lst, 0, n, 0, 0, results_lst)
    return results_lst
def generate_parentheses_recursive(str_lst, pos, n, open, close, results_lst):
    if close == n:
        result_str = "".join(str_lst)
        results_lst.append(result_str)
        return
    else:
        if open > close:
            str_lst[pos] = ')'
            generate_parentheses_recursive(str_lst, pos + 1, n, open, close + 1, results_lst)
        if open < n:
            str_lst[pos] = '('
            generate_parentheses_recursive(str_lst, pos + 1, n, open + 1, close, results_lst)
def generate_paths_up_right(n, k):
    if k == 0 and n == 0:
        return None
    if n < 0 or k < 0:
        return None
    generate_paths_up_right_recursive(n, k, "")
def generate_paths_up_right_recursive(n, k, prefix=''):
    if n == 0 and k == 0:
        print(prefix)
        return
    elif n == 0:
        generate_paths_up_right_recursive(n, k - 1, prefix + 'u')
        return
    elif k == 0:
        generate_paths_up_right_recursive(n - 1, k, prefix + 'r')
        return
    generate_paths_up_right_recursive(n, k - 1, prefix + 'u')
    generate_paths_up_right_recursive(n - 1, k, prefix + 'r')
def fill_surrounding(image, start):
    x, y = start
    flood_fill_recursive(image, x, y, '.', '*')
def flood_fill_recursive(image, x, y, empty_char, full_char):
    image_width = len(image)
    image_height = len(image[0])
    if image[x][y] != empty_char:
        return
    image[x][y] = full_char
    flood_fill_recursive(image, x - 1, y, empty_char, full_char)
    flood_fill_recursive(image, x, y - 1, empty_char, full_char)
    flood_fill_recursive(image, x + 1, y, empty_char, full_char)
    flood_fill_recursive(image, x, y + 1, empty_char, full_char)