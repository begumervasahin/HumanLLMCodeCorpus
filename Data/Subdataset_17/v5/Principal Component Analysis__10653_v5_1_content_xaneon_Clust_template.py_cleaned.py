import matplotlib.pyplot as plt
import numpy as np
def get(signal_chunks, showtemplate):
    n_signal_chunks = len(signal_chunks)
    signal_average = np.mean(signal_chunks, axis=0)
    std_quarter = np.mean(np.std(signal_chunks[:n_signal_chunks
    test_signal = signal_average.copy()
    test_signal[:len(test_signal)
    upper_limit = abs(test_signal) + (5 * std_quarter)
    lower_limit = signal_average - (7 * std_quarter)
    expanded_upper_limit = np.repeat(upper_limit, 4)
    start_idx = len(expanded_upper_limit)
    upper_limit_expanded = expanded_upper_limit[start_idx:start_idx + len(upper_limit)]
    if showtemplate:
        plt.plot(signal_average, label='Signal Average')
        plt.plot(upper_limit_expanded, 'r--', label='Upper Limit')
        plt.plot(lower_limit, 'r--', label='Lower Limit')
        plt.legend()
        plt.show()
    valid_signals = [
        np.all((chunk > lower_limit) & (chunk < upper_limit_expanded))
        for chunk in signal_chunks
    ]
    valid_indices = np.where(valid_signals)[0]
    print(f'{n_signal_chunks} signals have been reduced to {len(valid_indices)}.')
    return valid_indices