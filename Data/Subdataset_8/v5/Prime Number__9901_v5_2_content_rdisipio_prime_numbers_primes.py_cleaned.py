import sys
import numpy as np
import matplotlib.pyplot as plt
DEFAULT_ROWS = 24
DEFAULT_COLUMNS = 2
if len(sys.argv) > 1:
    columns = int(sys.argv[1])
else:
    columns = DEFAULT_COLUMNS
if len(sys.argv) > 2:
    rows = int(sys.argv[2])
else:
    rows = DEFAULT_ROWS
N_MAX = columns * rows
def primes(n):
    if n == 2:
        return [2]
    elif n < 2:
        return []
    sieve = list(range(3, n + 1, 2))
    mroot = n ** 0.5
    half = (n + 1)
    i = 0
    m = 3
    while m <= mroot:
        if sieve[i]:
            j = (m * m - 3)
            sieve[j] = 0
            while j < half:
                sieve[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in sieve if x]
known_primes = primes(N_MAX)
max_primes = len(known_primes)
if columns < 5:
    print(known_primes)
n_numbers = np.zeros(N_MAX)
r_numbers = np.zeros(N_MAX)
th_numbers = np.zeros(N_MAX)
n_primes = np.zeros(max_primes)
r_primes = np.zeros(max_primes)
th_primes = np.zeros(max_primes)
n = 0
p = 0
for c in range(columns):
    for i in range(rows):
        n_numbers[n] = n + 1
        r_numbers[n] = c + 1
        th_numbers[n] = (2. * np.pi / float(rows)) * (i + 1)
        if (p < max_primes) and (n_numbers[n] == known_primes[p]):
            n_primes[p] = n_numbers[n]
            r_primes[p] = r_numbers[n]
            th_primes[p] = th_numbers[n]
            p += 1
        n += 1
fig = plt.figure(figsize=(10., 10.))
ax = fig.add_subplot(111, projection="polar")
points_size = 100
font_size = 12
if columns > 10:
    points_size = 50
    font_size = 6
if columns > 30:
    points_size = 10
    font_size = 0
for x, y, n in zip(th_numbers, r_numbers, n_numbers):
    ax.scatter((x,), (y,), color="gray", s=points_size)
    if columns < 30:
        plt.text(x, y, '%i' % n, fontsize=font_size)
for x, y, n in zip(th_primes, r_primes, n_primes):
    ax.scatter((x,), (y,), color="red", s=points_size)
    if columns < 30:
        plt.text(x, y, '%i' % n, fontsize=font_size)
ax.set_rticks([])
dth = 360 / rows
ax.set_thetagrids([-dth, dth, 90 - dth, 90 + dth, 180 - dth, 180 + dth, 270 - dth, 270 + dth], labels=[''] * columns)
if columns > 1:
    ax.set_rgrids(np.arange(1, columns), labels=[''] * columns)
ax.grid(True)
ext = "jpg"
plt.savefig("%s/primes_r%i_c%i.%s" % (ext, rows, columns, ext))
plt.show()