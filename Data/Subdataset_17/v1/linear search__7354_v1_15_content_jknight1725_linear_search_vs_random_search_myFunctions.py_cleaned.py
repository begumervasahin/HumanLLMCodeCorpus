import random
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
    adjustment = '0'
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
    else:
        return "Error\n"
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
def print_time_report(time):
    print(f"Starts at: {time['start']}\nEnds at: {time['end']}\nTime taken to execute the function: {time['total']}\n")
def sum_up(large_num):
    return int((large_num * (large_num + 1)) / 2)
def get_three_random_numbers():
    x = random.randrange(10)
    y = random.randrange(10)
    z = random.randrange(10)
    return [x, y, z]
def prompt_for_num():
    return int(input("Enter a number: "))
def get_user_guesses():
    x = prompt_for_num()
    y = prompt_for_num()
    z = prompt_for_num()
    return [x, y, z]
def check_for_win(user_numbers, rand_numbers):
    return user_numbers == rand_numbers
def all_1000_options():
    options = []
    for x in range(0, 1000):
        x_str = str(x).zfill(3)
        options.append(x_str)
    return options
def worst_case_algorithm(options, three_random_numbers):
    idx = 0
    guesses = 1
    while [int(i) for i in str(options[idx])] != three_random_numbers:
        idx += 1
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