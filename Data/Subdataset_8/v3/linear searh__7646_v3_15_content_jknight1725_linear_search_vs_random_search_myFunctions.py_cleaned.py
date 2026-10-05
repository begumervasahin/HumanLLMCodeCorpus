from random import randrange
from time import process_time
def number_prompt(lower_bound, upper_bound):
    while True:
        num = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
        if lower_bound <= num <= upper_bound:
            return num
        else:
            print("Please enter a valid number.")
def prompt_for_num():
    return int(input("Enter a number: "))
def get_user_guesses():
    return [prompt_for_num() for _ in range(3)]
def computer_says(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def found(cpu_guess, guesses):
    print(f'Done! Your number is {cpu_guess}. Guessed in {guesses} times!')
def print_time_report(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}\n")
def get_adjustment():
    while True:
        adjustment = input("Type 'l' if larger, 's' if smaller, 'c' if correct: ").strip().lower()
        if adjustment in {'l', 's', 'c'}:
            return adjustment
def make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound):
    if adjustment == 'l':
        return [cpu_guess, upper_bound]
    elif adjustment == 's':
        return [lower_bound, cpu_guess]
    elif adjustment == 'c':
        return [lower_bound, upper_bound]
def check_for_win(user_numbers, rand_numbers):
    return user_numbers == rand_numbers
def measure_time(func, *args):
    start_time = process_time()
    result = func(*args)
    end_time = process_time()
    return result, end_time - start_time
def worst_case_algorithm(options, three_random_numbers):
    for idx, option in enumerate(options):
        if [int(i) for i in str(option)] == three_random_numbers:
            return idx + 1
def random_case_algorithm(three_random_numbers):
    upper_constraint = 5000
    guesses = 1
    while guesses < upper_constraint:
        if get_three_random_numbers() == three_random_numbers:
            return guesses
        guesses += 1
    return guesses
def sum_up(large_num):
    return int((large_num * (large_num + 1)) / 2)
def get_three_random_numbers():
    return [randrange(10) for _ in range(3)]
def all_1000_options():
    return [str(x).zfill(3) for x in range(1000)]
if __name__ == "__main__":
    pass
