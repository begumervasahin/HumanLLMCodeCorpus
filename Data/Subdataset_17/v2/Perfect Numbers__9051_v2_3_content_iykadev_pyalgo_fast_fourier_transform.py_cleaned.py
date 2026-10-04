from cmath import exp, pi
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even_part = fft(x[0::2])
    odd_part = fft(x[1::2])
    T = [exp(-2j * pi * k / N) * odd_part[k] for k in range(N
    return [even_part[k] + T[k] for k in range(N
           [even_part[k] - T[k] for k in range(N
sample_data = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0]
result = fft(sample_data)
formatted_result = ' '.join(f"{abs(f):5.3f}" for f in result)
print(formatted_result)