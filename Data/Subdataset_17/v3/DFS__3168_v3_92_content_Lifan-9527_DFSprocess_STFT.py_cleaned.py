
import math
import numpy as np
def stft(signal, window_length, slide_step):
    signal = np.asarray(signal)
    padded_length = 2 ** find_nearest_power_of_2(len(signal))
    if padded_length > len(signal):
        signal = np.pad(signal, (0, padded_length - len(signal)), mode='constant')
    num_windows = (len(signal) - window_length)
    window_matrix = np.zeros((window_length, num_windows))
    for i in range(num_windows):
        start_idx = slide_step * i
        end_idx = start_idx + window_length
        window_matrix[:, i] = signal[start_idx:end_idx]
    stft_result = np.fft.fft(window_matrix, axis=0)
    return stft_result
def find_nearest_power_of_2(n):
    if n <= 0:
        raise ValueError("Input must be greater than 0")
    power = 0
    while (1 << power) < n:
        power += 1
    return power
if __name__ == "__main__":
    signal = np.sin(2 * np.pi * np.arange(1000) / 100)
    window_length = 64
    slide_step = 32
    stft_result = stft(signal, window_length, slide_step)
    print("STFT result shape:", stft_result.shape)