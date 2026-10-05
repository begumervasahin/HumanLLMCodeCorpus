def list_to_string(char_list):
    return ''.join(char_list)
def print_numbers_up_to(n):
    if n < 1:
        return
    for i in range(1, n + 1):
        print(i)
def print_numbers_down_to(n):
    if n < 1:
        return
    for i in range(n, 0, -1):
        print(i)
def has_divisor_smaller_than(n, i):
    if i <= 1:
        return False
    if n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)
def is_prime(n):
    if n < 2:
        return False
    return not has_divisor_smaller_than(n, int(n ** 0.5))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
def exponential_limit(n, x):
    return (x ** n) / factorial(n) + exponential_limit(n - 1, x) if n > 0 else 1
def solve_hanoi_towers(hanoi, n, src, dest, temp):
    if n < 1:
        return
    if n == 1:
        hanoi.move(src, dest)
        return
    solve_hanoi_towers(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    solve_hanoi_towers(hanoi, n - 1, temp, dest, src)
def print_all_sequences(char_list, n):
    if n < 1:
        return
    print_sequences_recursive(char_list, "", n)
def print_sequences_recursive(char_list, prefix, k):
    if k == 0:
        print(prefix)
        return
    for char in char_list:
        new_prefix = prefix + char
        print_sequences_recursive(char_list, new_prefix, k - 1)
def print_unique_sequences(char_list, n):
    if n < 1:
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
    results_lst = []
    if n > 0:
        generate_parentheses_recursive([""] * 2 * n, 0, n, 0, 0, results_lst)
    return results_lst
def generate_parentheses_recursive(str_lst, pos, n, open_count, close_count, results_lst):
    if close_count == n:
        results_lst.append("".join(str_lst))
        return
    if open_count > close_count:
        str_lst[pos] = ')'
        generate_parentheses_recursive(str_lst, pos + 1, n, open_count, close_count + 1, results_lst)
    if open_count < n:
        str_lst[pos] = '('
        generate_parentheses_recursive(str_lst, pos + 1, n, open_count + 1, close_count, results_lst)
def generate_paths_up_right(n, k):
    if n < 0 or k < 0:
        return None
    generate_paths_up_right_recursive(n, k, "")
def generate_paths_up_right_recursive(n, k, prefix=''):
    if n == 0 and k == 0:
        print(prefix)
        return
    if n > 0:
        generate_paths_up_right_recursive(n - 1, k, prefix + 'r')
    if k > 0:
        generate_paths_up_right_recursive(n, k - 1, prefix + 'u')
def fill_surrounding(image, start):
    x, y = start
    flood_fill_recursive(image, x, y, '.', '*')
def flood_fill_recursive(image, x, y, empty_char, full_char):
    if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]) or image[x][y] != empty_char:
        return
    image[x][y] = full_char
    flood_fill_recursive(image, x - 1, y, empty_char, full_char)
    flood_fill_recursive(image, x, y - 1, empty_char, full_char)
    flood_fill_recursive(image, x + 1, y, empty_char, full_char)
    flood_fill_recursive(image, x, y + 1, empty_char, full_char)