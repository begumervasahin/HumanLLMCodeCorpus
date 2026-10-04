import sys
import numpy as np
import matplotlib.pyplot as plt
DEFAULT_ROWS = 24
DEFAULT_COLUMNS = 2
def parse_arguments():
    columns = DEFAULT_COLUMNS
    rows = DEFAULT_ROWS
    if len(sys.argv) > 1:
        columns = int(sys.argv[1])
    if len(sys.argv) > 2:
        rows = int(sys.argv[2])
    return columns, rows
def generate_primes(n):
    if n < 2:
        return []
    if n == 2:
        return [2]
    s = list(range(3, n + 1, 2))
    mroot = int(n ** 0.5)
    half = (n + 1)
    i = 0
    m = 3
    while m <= mroot:
        if s[i]:
            j = (m * m - 3)
            s[j] = 0
            while j < half:
                s[j] = 0
                j += m
        i += 1
        m = 2 * i + 3
    return [2] + [x for x in s if x]
def prepare_data_for_plotting(columns, rows, max_number, primes):
    total_numbers = columns * rows
    n_numbers = np.zeros(total_numbers)
    r_numbers = np.zeros(total_numbers)
    th_numbers = np.zeros(total_numbers)
    n_primes = np.zeros(len(primes))
    r_primes = np.zeros(len(primes))
    th_primes = np.zeros(len(primes))
    n = 0
    p = 0
    for c in range(columns):
        for i in range(rows):
            n_numbers[n] = n + 1
            r_numbers[n] = c + 1
            th_numbers[n] = (2. * np.pi / rows) * (i + 1)
            if p < len(primes) and n_numbers[n] == primes[p]:
                n_primes[p] = n_numbers[n]
                r_primes[p] = r_numbers[n]
                th_primes[p] = th_numbers[n]
                p += 1
            n += 1
    return n_numbers, r_numbers, th_numbers, n_primes, r_primes, th_primes
def plot_primes(columns, rows, n_numbers, r_numbers, th_numbers, n_primes, r_primes, th_primes):
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
            plt.text(x, y, f'{int(n)}', fontsize=font_size)
    for x, y, n in zip(th_primes, r_primes, n_primes):
        ax.scatter((x,), (y,), color="red", s=points_size)
        if columns < 30:
            plt.text(x, y, f'{int(n)}', fontsize=font_size)
    ax.set_rticks([])
    dth = 360 / rows
    ax.set_thetagrids([0, 90, 180, 270], labels=[''] * 4)
    if columns > 1:
        ax.set_rgrids(np.arange(1, columns + 1), labels=[''] * columns)
    ax.grid(True)
    plt.savefig(f"primes_r{rows}_c{columns}.jpg")
    plt.show()
def main():
    columns, rows = parse_arguments()
    max_number = columns * rows
    primes_list = generate_primes(max_number)
    if columns < 5:
        print(primes_list)
    data = prepare_data_for_plotting(columns, rows, max_number, primes_list)
    plot_primes(columns, rows, *data)
if __name__ == "__main__":
    main()