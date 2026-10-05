
def list_to_string(lst):
    return ''.join(lst)
def print_increasing(n):
    if n >= 1:
        print_increasing(n - 1)
        print(str(n))
    else:
        return
def print_decreasing(n):
    if n >= 1:
        print(str(n))
        print_decreasing(n - 1)
def has_smaller_divisor(n, i):
    if i == 1 or i == 0:
        return False
    elif n % i == 0:
        return True
    return has_smaller_divisor(n, i - 1)
def is_prime_number(n):
    if n < 2:
        return False
    i = int(n**0.5)
    if not has_smaller_divisor(n, i):
        return True
    return False
def calculate_factorial(n):
    if n == 1:
        return 1
    return n * calculate_factorial(n - 1)
def exponential_limit(n, x):
    if n == 0:
        return 1
    return (x ** n) / calculate_factorial(n) + exponential_limit(n - 1, x)
def print_word_sequences(char_list, n):
    if n == 0:
        return
    num_chars = n
    n = len(set(char_list))
    print_word_sequences_rec(char_list, "", n, num_chars)
def print_word_sequences_rec(char_list, prefix, num_chars, remaining_chars):
    if remaining_chars == 0:
        print(prefix)
        return
    for i in range(num_chars):
        new_prefix = prefix + char_list[i]
        print_word_sequences_rec(char_list, new_prefix, num_chars, remaining_chars - 1)
def print_unique_sequences(char_list, n):
    if n == 0:
        return
    print_unique_sequences_rec(char_list, "", n)
def print_unique_sequences_rec(char_list, prefix, n):
    if n == 0:
        print(prefix)
        return
    for i, char in enumerate(char_list):
        new_prefix = prefix + char
        print_unique_sequences_rec(char_list[:i] + char_list[i+1:], new_prefix, n-1)
def generate_parentheses(n):
    parentheses_list = [""] * 2 * n
    results_list = []
    if n > 0:
        generate_parentheses_rec(parentheses_list, 0, n, 0, 0, results_list)
    return results_list
def generate_parentheses_rec(parentheses_list, pos, n, open_count, close_count, results_list):
    if close_count == n:
        combination = "".join(parentheses_list)
        results_list.append(combination)
        return
    else:
        if open_count > close_count:
            parentheses_list[pos] = ")"
            generate_parentheses_rec(parentheses_list, pos + 1, n, open_count, close_count + 1, results_list)
        if open_count < n:
            parentheses_list[pos] = "("
            generate_parentheses_rec(parentheses_list, pos + 1, n, open_count + 1, close_count, results_list)
def print_up_and_right_paths(n, k):
    if k == 0 and n == 0:
        return None
    if n < 0 or k < 0:
        return None
    print_up_and_right_paths_rec(n, k, "")
def print_up_and_right_paths_rec(n, k, prefix=''):
    if n == 0 and k == 0:
        print(prefix)
        return
    elif n == 0:
        print_up_and_right_paths_rec(n, k - 1, prefix + 'u')
        return
    elif k == 0:
        print_up_and_right_paths_rec(n - 1, k, prefix + 'r')
        return
    print_up_and_right_paths_rec(n, k - 1, prefix + 'u')
    print_up_and_right_paths_rec(n - 1, k, prefix + 'r')
def flood_fill(image, start):
    x, y = start
    flood_fill_recursive(image, x, y, '.', '*')
def flood_fill_recursive(image, x, y, empty_char, fill_char):
    image_width = len(image)
    image_height = len(image[0])
    if image[x][y] != empty_char:
        return
    image[x][y] = fill_char
    flood_fill_recursive(image, x - 1, y, empty_char, fill_char)
    flood_fill_recursive(image, x, y - 1, empty_char, fill_char)
    flood_fill_recursive(image, x + 1, y, empty_char, fill_char)
    flood_fill_recursive(image, x, y + 1, empty_char, fill_char)
