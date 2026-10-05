from time import time
PAD_LEN = 1024 * 100
def valid_ptc(c):
    return ((64 < c < 91) or
            (96 < c < 123) or
            (47 < c < 58) or
            (c == 43) or
            (c == 47) or
            (c == 61))
def split_ct():
    a = [[] for _ in range(PAD_LEN)]
    with open('out', 'rb') as f:
        i = 0
        done = False
        while not done:
            c = f.read(1)
            if c != b'':
                a[i % PAD_LEN] += [ord(c)]
                i += 1
                continue
            done = True
    return a
def find_pad():
    a = split_ct()
    ka = [[] for _ in range(PAD_LEN)]
    j = 0
    t = time()
    for j in range(PAD_LEN):
        chk = a[j]
        gk = []
        for i in range(2 ** 8):
            b = False
            for c in chk:
                if valid_ptc(c ^ i):
                    continue
                b = True
            if not b:
                gk += [i]
        if len(gk) > 1:
            print('ka[{}]: {}'.format(j, gk))
        ka[j] = gk
        if time() - t > 5:
            t = time()
            print('Progress: {:4f}%'.format(100 * (float(j) / PAD_LEN)))
    write_key(ka)
def write_key(k):
    with open('key', 'w') as f:
        f.write(str(k))
def read_key():
    with open('key', 'r') as f:
        k = eval(f.read())
    return k
if __name__ == '__main__':
    k = read_key()
    f = ''
    with open('out', 'rb') as f_in:
        f = f_in.read()
    p = ''.join([chr(f[i] ^ k[i][0]) for i in range(PAD_LEN)])
    print(p)