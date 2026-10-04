def to_string(lst):
    return ''.join(lst)
def print_to_n(n):
    if n >= 1:
        print_to_n(n - 1)
        print(n)
def print_reversed(n):
    if n >= 1:
        print(n)
        print_reversed(n - 1)
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
    return not has_divisor_smaller_than(n, i)
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
def exp_n_x(n, x):
    if n == 0:
        return 1
    return (x ** n) / factorial(n) + exp_n_x(n - 1, x)
def play_hanoi(hanoi, n, src, dest, temp):
    if n < 1:
        return
    elif n == 1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)
def print_sequences(char_list, n):
    if n == 0:
        return
    unique_chars = list(set(char_list))
    _print_sequences_rec(unique_chars, "", len(unique_chars), n)
def _print_sequences_rec(char_list, prefix, n, k):
    if k == 0:
        print(prefix)
        return
    for i in range(n):
        new_prefix = prefix + char_list[i]
        _print_sequences_rec(char_list, new_prefix, n, k - 1)
def print_no_repetition_sequences(char_list, n):
    if n == 0:
        return
    _print_no_repetition_sequences_rec(char_list, "", n)
def _print_no_repetition_sequences_rec(char_list, prefix, n):
    if n == 0:
        print(prefix)
        return
    for i, char in enumerate(char_list):
        new_prefix = prefix + char
        _print_no_repetition_sequences_rec(char_list[:i] + char_list[i+1:], new_prefix, n - 1)
def parentheses(n):
    result_list = []
    if n > 0:
        _parentheses_rec([""] * 2 * n, 0, n, 0, 0, result_list)
    return result_list
def _parentheses_rec(curr, pos, n, open_count, close_count, result_list):
    if close_count == n:
        result_list.append("".join(curr))
        return
    if open_count > close_count:
        curr[pos] = ')'
        _parentheses_rec(curr, pos + 1, n, open_count, close_count + 1, result_list)
    if open_count < n:
        curr[pos] = '('
        _parentheses_rec(curr, pos + 1, n, open_count + 1, close_count, result_list)
def up_and_right(n, k):
    if n < 0 or k < 0:
        return None
    _up_and_right_rec(n, k, "")
def _up_and_right_rec(n, k, prefix):
    if n == 0 and k == 0:
        print(prefix)
        return
    if n > 0:
        _up_and_right_rec(n - 1, k, prefix + 'r')
    if k > 0:
        _up_and_right_rec(n, k - 1, prefix + 'u')
def flood_fill(image, start):
    x, y = start
    _flood_fill_rec(image, x, y, '.', '*')
def _flood_fill_rec(image, x, y, empty_char, fill_char):
    image_width = len(image)
    image_height = len(image[0])
    if x < 0 or x >= image_width or y < 0 or y >= image_height or image[x][y] != empty_char:
        return
    image[x][y] = fill_char
    _flood_fill_rec(image, x - 1, y, empty_char, fill_char)
    _flood_fill_rec(image, x + 1, y, empty_char, fill_char)
    _flood_fill_rec(image, x, y - 1, empty_char, fill_char)
    _flood_fill_rec(image, x, y + 1, empty_char, fill_char)