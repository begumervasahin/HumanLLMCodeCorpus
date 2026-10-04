import time
from visualize import plot_error, plot
KM_PER_MI = 1.60934
MI_PER_KM = 0.621371
def fib(n):
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
def load_fib(file_path='fib.csv'):
    fib_list = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                fib_list.append(float(line))
            if len(fib_list) >= 1000:
                break
    return fib_list
def km_to_mi(km):
    return km * MI_PER_KM
def mi_to_km(mi):
    return mi * KM_PER_MI
def calculate_loss(index, fib_list):
    mi = fib_list[index]
    fib_km = fib_list[index + 1]
    actual_km = mi_to_km(mi)
    return abs((actual_km - fib_km) / actual_km) * 100
def main():
    fib_list = load_fib()
    for i in range(1, len(fib_list) - 1):
        error = calculate_loss(i, fib_list)
        plot_error(i, error, 'Error', 'Fibonacci Index')
        plot(i, fib_list[i], 'Fibonacci Index', 'Distance', 'Miles')
        plot(i, fib_list[i + 1], 'Fibonacci Index', 'Distance', 'Kilometers')
        time.sleep(0.2)
if __name__ == "__main__":
    main()