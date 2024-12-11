from __future__ import print_function, division
from CPUtimer import CPUTimer
from data2 import instance_iterator, print_solution
def fonk1(b6):
    b1 = CPUTimer()
    for instance in instance_iterator(b6):
        instance_name, capacity, values, b2 = instance
        b1.reset()
        b1.start()
        for b5 in range(2):
            b3 = fonk2(capacity, values, b2)
            b1.lap()
        b1.stop()
        print_solution(values, b2, b3, instance_name, '2a', b1)
def fonk2(capacity, values, b2):
    b3 = [(i + 1, w, v / w) for i, (v, w) in enumerate(zip(values, b2))]
    b3 = iter(sorted(b3, key=lambda t: t[2], reverse=True))
    b4 = [0] * len(values)
    a1 = 0
    while a1 < capacity:
        try:
            item_idx, item_weight, b5 = next(b3)
            if a1 + item_weight <= capacity:
                b4[item_idx - 1] = 1
                a1 += item_weight
            else:
                b4[item_idx - 1] = (capacity - a1) / item_weight
                a1 = capacity
        except StopIteration:
            break
    return [(i + 1, fraction) for i, fraction in enumerate(b4) if fraction > 0]
b6 = "path_to_instance_file"
fonk1(b6)