from __future__ import print_function, division
from CPUtimer import CPUTimer
from data2 import instance_iterator, print_solution
def solve(instance_path):
    timer = CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, capacity, values, weights = instance
        timer.reset()
        timer.start()
        for _ in range(2):
            items = knapsack(capacity, values, weights)
            timer.lap()
        timer.stop()
        print_solution(values, weights, items, instance_name, '2a', timer)
def knapsack(capacity, values, weights):
    items = [(i + 1, w, v / w) for i, (v, w) in enumerate(zip(values, weights))]
    items = sorted(items, key=lambda t: t[2], reverse=True)
    selected_items = [0] * len(values)
    total_weight = 0
    for i, w, _ in items:
        if total_weight + w <= capacity:
            selected_items[i - 1] = 1
            total_weight += w
        else:
            selected_items[i - 1] = (capacity - total_weight) / w
            total_weight = capacity
            break
    return [(i + 1, fract) for i, fract in enumerate(selected_items) if fract > 0]
instance_path = "path_to_instance_file"
solve(instance_path)