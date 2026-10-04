from __future__ import print_function, division
import CPUtimer
from data2 import instance_iterator, print_solution
def fonk1(b7):
    b1 = CPUtimer.CPUTimer()
    for instance in instance_iterator(b7):
        instance_name, capacity, profits, b2 = instance
        b1.reset()
        b1.start()
        for b5 in range(2):
            b3 = fonk2(capacity, profits, b2)
            b1.lap()
        b1.stop()
        print_solution(profits, b2, b3, instance_name, '2a', b1)
def fonk2(capacity, profits, b2):
    b3 = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(profits, b2))]
    b3 = iter(sorted(b3, key=lambda item: item[2], reverse=True))
    b4 = [0] * len(profits)
    a1 = 0
    while a1 < capacity:
        try:
            i, w, b5 = next(b3)
            if a1 + w <= capacity:
                b4[i - 1] = 1
                a1 += w
            else:
                b4[i - 1] = (capacity - a1) / w
                a1 = capacity
        except StopIteration:
            break
    return [(i + 1, frac) for i, frac in enumerate(b4) if frac > 0]
if b6 = = "__main__":
    b7 = 'path_to_instance_file'
    fonk1(b7)