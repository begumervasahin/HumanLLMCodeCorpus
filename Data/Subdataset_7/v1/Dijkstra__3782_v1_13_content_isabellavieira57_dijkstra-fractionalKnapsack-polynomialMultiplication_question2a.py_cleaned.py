from __future__ import print_function, division
from CPUtimer import CPUTimer
from data2 import instance_iterator, print_solution
def fonk1(b6):
    b1 = CPUTimer()
    for instance in instance_iterator(b6):
        instance_name, k, P, b2 = instance
        b1.reset()
        b1.start()
        for i in range(0, 2):
            b3 = fonk2(k, P, b2)
            b1.lap()
        b1.stop()
        print_solution(P, b2, b3, instance_name, '2a', b1)
def fonk2(k, P, b2):
    b3 = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(P, b2))]
    b3 = iter(sorted(b3, key=lambda t: t[2], reverse=True))
    b4 = [0] * len(P)
    a1 = 0
    while a1 < k:
        try:
            i, w, b5 = next(b3)
            if a1 + w <= k:
                b4[i - 1] = 1
                a1 += w
            else:
                b4[i - 1] = (k - a1) / w
                a1 = k
        except StopIteration:
            break
    return [(i + 1, fract) for i, fract in enumerate(b4) if fract > 0]
b6 = "path_to_instance_file"
fonk1(b6)