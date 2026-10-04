def list_fib_seq(s, x):
    res = [0, s]
    while (res[-1] + res[-2] <= x):
        res.append(res[-1] + res[-2])
    print(res)
    return res
def find_fibish_seq_number(orgFs, x):
    min_start_int = None
    for member in orgFs:
        if member > x:
            break
        if member == 0 or member == 1:
            continue
        if x % member == 0:
            quotient = x
            if min_start_int is None or quotient < min_start_int:
                min_start_int = quotient
    return min_start_int
if __name__ == '__main__':
    INPUT_INTEGER = 464
    orig_fib_seq = list_fib_seq(1, INPUT_INTEGER)
    t = find_fibish_seq_number(orig_fib_seq, INPUT_INTEGER)
    if t is None:
        t = INPUT_INTEGER
    print(f"Min Integer Found: {t}")
    list_fib_seq(t, INPUT_INTEGER)