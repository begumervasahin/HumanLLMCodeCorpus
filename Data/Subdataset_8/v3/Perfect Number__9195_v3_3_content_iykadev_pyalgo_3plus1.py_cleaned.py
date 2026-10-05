def three_plus_one_sequence(x):
    iterations = 0
    while x > 1:
        iterations += 1
        if x % 2:
            x = 3 * x + 1
        else:
            x
        print(x)
    return iterations
def main():
    initial_value = 15000
    print(f"Starting 3n+1 sequence with initial value: {initial_value}")
    iterations_taken = three_plus_one_sequence(initial_value)
    print(f"Number of iterations taken: {iterations_taken}")
if __name__ == "__main__":
    main()