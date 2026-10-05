def list_fib_seq(s,x):
    res = [0,s]
    i = 2
    while (res[i-1] + res[i-2] <= x):
        res.append(res[i-1] + res[i-2])
        i += 1
    print res
    return res
def find_fibish_seq_number( orgFs, x):
    minStartInt = None
    for member in orgFs:
        if member > x:
            break
        if member == 0 or member == 1:
            continue
        if x % member == 0:
            if minStartInt is None:
                minStartInt = x/member
            else:
                if x/member <= minStartInt:
                    minStartInt = x/member
    return minStartInt
if __name__ == '__main__':
    INPUT_INTEGER = 464
    orig_fib_seq = list_fib_seq(1,INPUT_INTEGER)
    t = find_fibish_seq_number(orig_fib_seq, INPUT_INTEGER)
    if t is None:
        t = INPUT_INTEGER
    print "Min Interger Found:%d" % t
    list_fib_seq(t, INPUT_INTEGER)