import time
from visualize import plot_error, plot
KM_PER_MI = 1.60934
MI_PER_KM = 0.621371
def fib(n):
    if n <= 0:
        print("Invalid input")
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def load_fibonacci_numbers(file_path='fib.csv'):
    fibonacci_numbers = []
    with open(file_path, 'r') as file:
        for cnt, line in enumerate(file, start=1):
            line = line.strip()
            if line:
                fibonacci_numbers.append(float(line))
            if cnt >= 1000:
                break
    return fibonacci_numbers
def kilometers_to_miles(km):
    return km * MI_PER_KM
def miles_to_kilometers(mi):
    return mi * KM_PER_MI
def calculate_loss(index, fibonacci_numbers):
    miles = fibonacci_numbers[index]
    fibonacci_km = fibonacci_numbers[index + 1]
    actual_km = miles_to_kilometers(miles)
    return abs((actual_km - fibonacci_km) / actual_km) * 100
def main():
    fibonacci_numbers = load_fibonacci_numbers()
    for i in range(1, len(fibonacci_numbers) - 1):
        error = calculate_loss(i, fibonacci_numbers)
        plot_error(i, error, 'Error', 'Fibonacci Index')
        plot(i, fibonacci_numbers[i], 'Fibonacci Index', 'Distance', 'Miles')
        plot(i, fibonacci_numbers[i + 1], 'Fibonacci Index', 'Distance', 'Kilometers')
        time.sleep(0.2)
if __name__ == "__main__":
    main()