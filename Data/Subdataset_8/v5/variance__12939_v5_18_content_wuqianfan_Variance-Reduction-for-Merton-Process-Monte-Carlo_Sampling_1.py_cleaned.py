import numpy as np
import time
T = 1
s0 = 100
v0 = 0.12
kappa = 2
theta = 0.15
sigma = 0.8
r = 0
def simulate_heston(N):
    dt = T / N
    ST = s0
    VT = v0
    for _ in range(N):
        dW_s = np.random.randn() * np.sqrt(dt)
        dW_v = np.random.randn() * np.sqrt(dt)
        ST += r * ST * dt + np.sqrt(max(VT, 0)) * ST * dW_s
        VT += kappa * (theta - VT) * dt + sigma * np.sqrt(max(VT, 0)) * dW_v
    return ST
strikes = [70, 90, 100, 110, 130]
num_steps = [100, 500, 1000, 5000, 10000]
num_paths = [int(np.sqrt(steps)) for steps in num_steps]
option_price_estimations = []
computation_times = []
for strike in strikes:
    price_estimations = []
    times = []
    for steps, paths in zip(num_steps, num_paths):
        start_time = time.time()
        sum_estimator = sum(np.maximum(simulate_heston(steps) - strike, 0) for _ in range(paths))
        option_price = np.exp(-r * T) * (sum_estimator / paths)
        end_time = time.time()
        price_estimations.append(option_price)
        times.append(end_time - start_time)
    option_price_estimations.append(price_estimations)
    computation_times.append(times)
correct_prices = [32.70326, 18.92499, 13.984957, 10.263762, 5.5888102]
print("Option Price Estimations:")
for i, strike in enumerate(strikes):
    print(f"For strike price {strike}: {option_price_estimations[i]}")
print("\nComputation Times:")
for i, strike in enumerate(strikes):
    print(f"For strike price {strike}: {computation_times[i]} seconds")
print("\nCorrect Option Prices:")
print(correct_prices)