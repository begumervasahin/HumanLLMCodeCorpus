from __future__ import print_function, division
from CPUtimer import CPUTimer
from data2 import instance_iterator, print_solution
def fonk1(b5):
    b1 = CPUTimer()
    for instance in instance_iterator(b5):
        instance_name, capacity, values, b2 = instance
        b1.reset()
        b1.start()
        for _ in range(2):
            b3 = fonk2(capacity, values, b2)
            b1.lap()
        b1.stop()
        print_solution(values, b2, b3, instance_name, '2a', b1)
def fonk2(capacity, values, b2):
    b3 = [(i + 1, w, v / w) for i, (v, w) in enumerate(zip(values, b2))]
    b3 = sorted(b3, key=lambda t: t[2], reverse=True)
    b4 = [0] * len(values)
    a1 = 0
    for i, w, _ in b3:
        if a1 + w <= capacity:
            b4[i - 1] = 1
            a1 += w
        else:
            b4[i - 1] = (capacity - a1) / w
            a1 = capacity
            break
    return [(i + 1, fract) for i, fract in enumerate(b4) if fract > 0]
b5 = "path_to_instance_file"
fonk1(b5)