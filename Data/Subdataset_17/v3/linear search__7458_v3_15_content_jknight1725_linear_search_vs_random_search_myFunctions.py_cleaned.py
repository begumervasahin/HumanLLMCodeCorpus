import random
from time import process_time
def number_prompt(lower_bound, upper_bound):
    while True:
        try:
            num = int(input(f"Enter a number between {lower_bound} and {upper_bound}: "))
            if lower_bound <= num <= upper_bound:
                return num
        except ValueError:
            pass
        print(f"Invalid input. Please enter a number between {lower_bound} and {upper_bound}.")
def compare_prompt():
    return "Type 'l' if larger, 's' if smaller, 'c' if correct: "
def computer_says(cpu_guess):
    print(f'Computer says: {cpu_guess}')
def mid(lower, upper):
    return (upper + lower)
def get_adjustment():
    while True:
        adjustment = input(compare_prompt()).lower()
        if adjustment in ['l', 's', 'c']:
            return adjustment
def make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound):
    if adjustment == 'l':
        return cpu_guess, upper_bound
    elif adjustment == 's':
        return lower_bound, cpu_guess
    elif adjustment == 'c':
        return lower_bound, upper_bound
def found(cpu_guess, guesses):
    print(f'Done! Your number is {cpu_guess}. Guessed in {guesses} times!')
def time_efficiency(func, *args):
    start_time = process_time()
    func(*args)
    end_time = process_time()
    return {
        'start': start_time,
        'end': end_time,
        'total': end_time - start_time
    }
def print_time_report(time_report):
    print(f"Starts at: {time_report['start']}\nEnds at: {time_report['end']}\nTime taken to execute the function: {time_report['total']}")
def sum_up(large_num):
    return large_num * (large_num + 1)
def get_three_random_numbers():
    return [random.randint(0, 9) for _ in range(3)]
def prompt_for_num():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_user_guesses():
    return [prompt_for_num() for _ in range(3)]
def check_for_win(user_numbers, rand_numbers):
    return user_numbers == rand_numbers
def all_1000_options():
    return [str(x).zfill(3) for x in range(1000)]
def worst_case_algorithm(options, three_random_numbers):
    guesses = 0
    for option in options:
        guesses += 1
        if [int(digit) for digit in option] == three_random_numbers:
            break
    return guesses
def random_case_algorithm(three_random_numbers):
    upper_constraint = 5000
    guesses = 0
    while guesses < upper_constraint:
        guesses += 1
        if get_three_random_numbers() == three_random_numbers:
            break
    return guesses
if __name__ == "__main__":
    lower_bound = 1
    upper_bound = 100
    number = number_prompt(lower_bound, upper_bound)
    guesses = 0
    found_number = False
    while not found_number:
        cpu_guess = mid(lower_bound, upper_bound)
        computer_says(cpu_guess)
        adjustment = get_adjustment()
        lower_bound, upper_bound = make_adjustment(adjustment, cpu_guess, lower_bound, upper_bound)
        guesses += 1
        if adjustment == 'c':
            found_number = True
            found(cpu_guess, guesses)
    time_report = time_efficiency(sum_up, 1000000)
    print_time_report(time_report)
    random_numbers = get_three_random_numbers()
    user_guesses = get_user_guesses()
    if check_for_win(user_guesses, random_numbers):
        print("Congratulations! You guessed correctly.")
    else:
        print("Sorry, better luck next time.")
    options = all_1000_options()
    guesses = worst_case_algorithm(options, random_numbers)
    print(f'Worst case algorithm guessed in {guesses} tries.')
    guesses = random_case_algorithm(random_numbers)
    print(f'Random case algorithm guessed in {guesses} tries.')