def collatz_sequence(n):
    step_count = 0
    while n > 1:
        step_count += 1
        if n % 2:
            n = 3 * n + 1
        else:
            n = n / 2
        print(n)
def main_collatz_sequence(starting_number):
    collatz_sequence(starting_number)
main_collatz_sequence(15000)