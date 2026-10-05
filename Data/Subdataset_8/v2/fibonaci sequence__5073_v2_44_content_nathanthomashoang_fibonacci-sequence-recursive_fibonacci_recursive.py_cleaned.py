def recursive_fibo(num):
    '''Calculate the Fibonacci value recursively.'''
    if num <= 1:
        return num
    return recursive_fibo(num - 2) + recursive_fibo(num - 1)
def run_fibonacci_program():
    '''Run the Fibonacci program.'''
    while True:
        try:
            term = int(input('How many Fibonacci terms would you like to generate?: '))
        except ValueError:
            print('\nPlease enter an integer.')
        else:
            if term <= 0:
                print("\nPlease enter a positive integer.")
            else:
                break
    print("\nGenerated Fibonacci sequence:\n")
    for num in range(term + 1):
        print(recursive_fibo(num))
if __name__ == "__main__":
    run_fibonacci_program()