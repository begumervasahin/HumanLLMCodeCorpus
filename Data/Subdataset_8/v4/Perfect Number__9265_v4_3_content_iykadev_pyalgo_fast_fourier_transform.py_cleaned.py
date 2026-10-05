from cmath import exp, pi
def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd =  fft(x[1::2])
    T = [exp(-2j*pi*k/N)*odd[k] for k in range(N
    return [even[k] + T[k] for k in range(N
           [even[k] - T[k] for k in range(N
result = fft([1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0])
formatted_result = ' '.join("%5.3f" % abs(f) for f in result)
print(formatted_result)