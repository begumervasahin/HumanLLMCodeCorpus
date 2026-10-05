import sys
import time
from visualize import plot_error, plot
KM_PER_MI = 1.60934
MI_PER_KM = 0.621371
def fib(n):
    if n <= 0:
        print("Invalid input")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
def load_fib():
    fib_list = [0]
    with open('fib.csv') as fp:
        cnt = 1
        for line in fp:
            if cnt >= 1000:
                break
            fib_list.append(float(line.strip()))
            cnt += 1
    return fib_list
def km_to_mi(km):
    return km * MI_PER_KM
def mi_to_km(mi):
    return mi * KM_PER_MI
def calculate_loss(n, fib_list):
    mi = fib_list[n]
    fib_km = fib_list[n+1]
    actual_km = mi_to_km(mi)
    return abs((actual_km - fib_km) / actual_km) * 100
fib_list = load_fib()
i = 1
while i < len(fib_list):
    error = calculate_loss(i, fib_list)
    plot_error(i, error, 'Error', 'Fibonacci Index')
    plot(i, fib_list[i], 'Fibonacci Index', 'Distance', 'mi', '')
    plot(i, fib_list[i+1], 'Fibonacci Index', 'Distance', 'km', '')
    time.sleep(0.2)
    i += 1