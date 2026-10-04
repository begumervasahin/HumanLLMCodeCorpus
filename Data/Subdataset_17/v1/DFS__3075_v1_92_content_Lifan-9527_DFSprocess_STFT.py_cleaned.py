
import math
import numpy as np
def stft(source, winlen, slide):
    data = np.asarray(source)
    topindex = 2 ** power2_near(len(data))
    if topindex - len(data) > 0:
        data = np.pad(data, (0, topindex - len(data)), mode='constant')
    win_num = int((len(data) - winlen) / slide) + 1
    window_matrix = np.zeros((winlen, win_num))
    for i in range(win_num):
        window_matrix[:, i] = data[slide * i:slide * i + winlen]
    complex_map = np.fft.fft(window_matrix, axis=0)
    return complex_map
def power2_near(k):
    assert k > 0, "Input must be greater than 0"
    power = 0
    while k > 1:
        k = math.ceil(k / 2)
        power += 1
    return power
if __name__ == "__main__":
    signal = np.sin(2 * np.pi * np.arange(1000) / 100)
    window_length = 64
    slide_step = 32
    stft_result = stft(signal, window_length, slide_step)
    print("STFT result shape:", stft_result.shape)