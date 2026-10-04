import sys
import numpy as np
import matplotlib.pyplot as plt
R = 24
C = 2
if len(sys.argv) > 1:
    C = int(sys.argv[1])
if len(sys.argv) > 2:
    R = int(sys.argv[2])
N_max = C * R
def generate_primes(n):
    if n < 2:
        return []
    sieve = np.ones(n
    for i in range(1, int(n**0.5)
        if sieve[i]:
            sieve[2*i*(i+1)::2*i+1] = False
    return [2] + [2*i+1 for i in range(1, n
known_primes = generate_primes(N_max)
max_primes = len(known_primes)
if C < 5:
    print(known_primes)
n_numbers = np.arange(1, N_max + 1)
r_numbers = np.repeat(np.arange(1, C + 1), R)
th_numbers = np.tile(np.linspace(0, 2 * np.pi, R, endpoint=False), C)
n_primes = np.array([n for n in known_primes if n <= N_max])
r_primes = r_numbers[np.isin(n_numbers, n_primes)]
th_primes = th_numbers[np.isin(n_numbers, n_primes)]
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection="polar")
points_size = 100 if C <= 10 else 50 if C <= 30 else 10
font_size = 12 if C <= 10 else 6 if C <= 30 else 0
ax.scatter(th_numbers, r_numbers, color="gray", s=points_size)
if C < 30:
    for x, y, n in zip(th_numbers, r_numbers, n_numbers):
        ax.text(x, y, f'{n}', fontsize=font_size)
ax.scatter(th_primes, r_primes, color="red", s=points_size)
if C < 30:
    for x, y, n in zip(th_primes, r_primes, n_primes):
        ax.text(x, y, f'{n}', fontsize=font_size)
ax.set_rticks([])
ax.set_thetagrids(range(0, 360, int(360 / R)), labels=[''] * R)
if C > 1:
    ax.set_rgrids(np.arange(1, C + 1), labels=[''] * C)
ax.grid(True)
plt.savefig(f"primes_r{R}_c{C}.jpg")
plt.show()