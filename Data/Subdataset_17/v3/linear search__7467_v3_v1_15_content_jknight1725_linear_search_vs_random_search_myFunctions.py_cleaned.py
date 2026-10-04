from random import randrange
from time import process_time
def number_prompt(lower_bound, upper_bound):
    num = -1
    while num < lower_bound or num > upper_bound:
        num = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
    return num
def compare_prompt():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def computer_says(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def mid(lower, upper):
    return (upper + lower)
def get_adjustment():
    adjustment = ''
    while adjustment not in 'lsc':
        adjustment = input(compare_prompt())[0]
    return adjustment
def make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound):
    if adjustment == 'l':
        return [cpu_guess, upper_bound]
    elif adjustment == 's':
        return [lower_bound, cpu_guess]
    elif adjustment == 'c':
        return [lower_bound, upper_bound]
def found(cpu_guess, guesses):
    print(f'Done! Your number is {cpu_guess}. Guessed in {guesses} attempts!')
def time_efficiency(func, *args):
    start_time = process_time()
    func(*args)
    end_time = process_time()
    return {
        'start': start_time,
        'end': end_time,
        'total': end_time - start_time
    }
def print_time_report(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']} seconds\n")
def sum_up(large_num):
    return int((large_num * (large_num + 1)) / 2)
def get_three_random_numbers():
    return [randrange(10) for _ in range(3)]
def prompt_for_num(prompt_text="Enter a number: "):
    return int(input(prompt_text))
def get_user_guesses():
    return [prompt_for_num() for _ in range(3)]
def check_for_win(user_numbers, rand_numbers):
    return user_numbers == rand_numbers
def all_1000_options():
    return [f"{x:03d}" for x in range(1000)]
def worst_case_algorithm(options, three_random_numbers):
    guesses = 1
    for idx in range(len(options)):
        if [int(digit) for digit in options[idx]] == three_random_numbers:
            break
        guesses += 1
    return guesses
def random_case_algorithm(three_random_numbers):
    upper_constraint = 5000
    guesses = 1
    while get_three_random_numbers() != three_random_numbers and guesses < upper_constraint:
        guesses += 1
    return guesses
if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 100
    user_number = number_prompt(lower_bound, upper_bound)
    guesses = 0
    lower = lower_bound
    upper = upper_bound
    cpu_guess = mid(lower, upper)
    while True:
        computer_says(cpu_guess)
        adjustment = get_adjustment()
        if adjustment == 'c':
            guesses += 1
            found(cpu_guess, guesses)
            break
        lower, upper = make_adjustment(adjustment, cpu_guess, lower, upper)
        cpu_guess = mid(lower, upper)
        guesses += 1
    large_num = 1000000
    time_report = time_efficiency(sum_up, large_num)
    print_time_report(time_report)
    random_numbers = get_three_random_numbers()
    user_guesses = get_user_guesses()
    if check_for_win(user_guesses, random_numbers):
        print("You win!")
    else:
        print("Try again!")
    options = all_1000_options()
    guesses = worst_case_algorithm(options, random_numbers)
    print(f"Worst case guesses: {guesses}")
    guesses = random_case_algorithm(random_numbers)
    print(f"Random case guesses: {guesses}")