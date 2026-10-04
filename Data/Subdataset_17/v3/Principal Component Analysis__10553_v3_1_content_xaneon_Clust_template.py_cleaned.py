import matplotlib.pyplot as plt
import numpy as np
def calculate_limits(signal_chunks, signal_average, std_quarter):
    test_signal = signal_average.copy()
    test_signal[:len(test_signal)
    upper_limit = np.abs(test_signal) + (5 * std_quarter)
    lower_limit = signal_average.mean() * np.ones(len(signal_average)) - (7 * std_quarter)
    upper_limit_extended = np.repeat(upper_limit, 2)
    start_idx = int(len(upper_limit_extended) / (4 / 1.5)) + int(4 * 1.5)
    upper_limit_adjusted = upper_limit_extended[start_idx:start_idx + len(upper_limit)]
    return upper_limit_adjusted, lower_limit
def plot_signal_template(signal_average, upper_limit, lower_limit):
    plt.plot(signal_average, label='Signal Average')
    plt.plot(upper_limit, 'r--', label='Upper Limit')
    plt.plot(lower_limit, 'r--', label='Lower Limit')
    plt.legend()
    plt.show()
def filter_signals(signal_chunks, upper_limit, lower_limit):
    valid_signals = []
    for signal in signal_chunks:
        within_limits = np.logical_and(signal > lower_limit, signal < upper_limit)
        valid_signals.append(np.all(within_limits))
    valid_indices = np.where(valid_signals)[0]
    return valid_indices
def get(signal_chunks, showtemplate):
    n_signal_chunks = len(signal_chunks)
    signal_average = np.mean(signal_chunks, axis=0)
    std_quarter = np.mean(np.std(signal_chunks[:n_signal_chunks
    upper_limit, lower_limit = calculate_limits(signal_chunks, signal_average, std_quarter)
    if showtemplate:
        plot_signal_template(signal_average, upper_limit, lower_limit)
    valid_indices = filter_signals(signal_chunks, upper_limit, lower_limit)
    print(f'{n_signal_chunks} signals have been reduced to {len(valid_indices)}.\n')
    return valid_indices
