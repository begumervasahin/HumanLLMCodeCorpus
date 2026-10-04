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
    if i <= 1:
        return False
    elif n % i == 0:
        return True
    return has_divisor_smaller_than(n, i - 1)
def is_prime(n):
    if n < 2:
        return False
    return not has_divisor_smaller_than(n, int(n ** 0.5))
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
    if n == 1:
        hanoi.move(src, dest)
        return
    play_hanoi(hanoi, n - 1, src, temp, dest)
    hanoi.move(src, dest)
    play_hanoi(hanoi, n - 1, temp, dest, src)
def print_sequences(char_list, n):
    if n == 0:
        return
    print_sequences_rec(char_list, "", len(set(char_list)), n)
def print_sequences_rec(char_list, prefix, n, k):
    if k == 0:
        print(prefix)
        return
    for i in range(n):
        new_prefix = prefix + char_list[i]
        print_sequences_rec(char_list, new_prefix, n, k - 1)
def print_no_repetition_sequences(char_list, n):
    if n == 0:
        return
    print_no_repetition_sequences_rec(char_list, "", n)
def print_no_repetition_sequences_rec(char_list, prefix, n):
    if n == 0:
        print(prefix)
        return
    for i, char in enumerate(char_list):
        new_prefix = prefix + char
        print_no_repetition_sequences_rec(char_list[:i] + char_list[i + 1:], new_prefix, n - 1)
def parentheses(n):
    result = []
    if n > 0:
        parentheses_rec([""] * 2 * n, 0, n, 0, 0, result)
    return result
def parentheses_rec(curr, pos, n, open, close, result):
    if close == n:
        result.append(to_string(curr))
        return
    if open > close:
        curr[pos] = ')'
        parentheses_rec(curr, pos + 1, n, open, close + 1, result)
    if open < n:
        curr[pos] = '('
        parentheses_rec(curr, pos + 1, n, open + 1, close, result)
def up_and_right(n, k):
    if n < 0 or k < 0:
        return
    up_and_right_rec(n, k, "")
def up_and_right_rec(n, k, prefix):
    if n == 0 and k == 0:
        print(prefix)
        return
    if n > 0:
        up_and_right_rec(n - 1, k, prefix + 'r')
    if k > 0:
        up_and_right_rec(n, k - 1, prefix + 'u')
def flood_fill(image, start):
    x, y = start
    flood_fill_rec(image, x, y, '.', '*')
def flood_fill_rec(image, x, y, empty_char, fill_char):
    width = len(image)
    height = len(image[0])
    if x < 0 or x >= width or y < 0 or y >= height or image[x][y] != empty_char:
        return
    image[x][y] = fill_char
    flood_fill_rec(image, x - 1, y, empty_char, fill_char)
    flood_fill_rec(image, x + 1, y, empty_char, fill_char)
    flood_fill_rec(image, x, y - 1, empty_char, fill_char)
    flood_fill_rec(image, x, y + 1, empty_char, fill_char)
if __name__ == "__main__":
    print("Sum of numbers up to 5:", sum_of_numbers(5))
    print("Is 3 a prime number?", is_prime(3))
    print("Factorial of 5:", factorial(5))
    print("Value of e^2 calculated up to 5 terms:", exp_n_x(5, 2))
    print("Printing numbers from 1 to 5:")
    print_to_n(5)
    print("Printing numbers from 5 to 1:")
    print_reversed(5)
    print("Printing sequences of length 3 from 'hello':")
    print_sequences(['h', 'e', 'l', 'l', 'o'], 3)
    print("Generating parentheses combinations for 3 pairs:")
    for combination in parentheses(3):
        print(combination)
    print("Possible paths from (0,0) to (2,2):")
    up_and_right(2, 2)
    image = [
        ['.', '.', '.', '.', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '*', '.', '*', '.'],
        ['.', '*', '*', '*', '.'],
        ['.', '.', '.', '.', '.']
    ]
    print("Flood fill from (2,2):")
    flood_fill(image, (2, 2))
    for row in image:
        print(''.join(row))