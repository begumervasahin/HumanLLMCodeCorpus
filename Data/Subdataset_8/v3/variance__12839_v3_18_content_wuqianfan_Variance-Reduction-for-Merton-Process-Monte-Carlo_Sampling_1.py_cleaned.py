import numpy as np
import matplotlib.pyplot as plt
import time
T = 1
s0 = 100
v0 = 0.12
kappa = 2
theta = 0.15
sigma = 0.8
r = 0
def simulate_path_Heston(N):
    dt = T / N
    ST = s0
    VT = v0
    for _ in range(N):
        ST += r * ST * dt + max(VT, 0) ** 0.5 * ST * dt ** 0.5 * np.random.randn()
        VT += kappa * (theta - VT) * dt + sigma * max(VT, 0) ** 0.5 * dt ** 0.5 * np.random.randn()
    return ST
strikes = [70, 90, 100, 110, 130]
num_simulations = [100, 500, 1000, 5000, 10000]
num_steps = [int(n ** 0.5) for n in num_simulations]
option_prices = []
execution_times = []
for strike in strikes:
    prices_for_strike = []
    times_for_strike = []
    for num_steps, num_sims in zip(num_steps, num_simulations):
        start_time = time.time()
        sim_results = [simulate_path_Heston(num_steps) for _ in range(num_sims)]
        option_price = np.mean([np.exp(-r * T) * max(ST - strike, 0) for ST in sim_results])
        end_time = time.time()
        prices_for_strike.append(option_price)
        times_for_strike.append(end_time - start_time)
    option_prices.append(prices_for_strike)
    execution_times.append(times_for_strike)
print("Option Price Estimations:")
for i, strike in enumerate(strikes):
    print(f"Strike: {strike}, Prices: {option_prices[i]}")
print("\nExecution Times:")
for i, strike in enumerate(strikes):
    print(f"Strike: {strike}, Times: {execution_times[i]}")
correct_prices = [32.70326, 18.92499, 13.984957, 10.263762, 5.5888102]