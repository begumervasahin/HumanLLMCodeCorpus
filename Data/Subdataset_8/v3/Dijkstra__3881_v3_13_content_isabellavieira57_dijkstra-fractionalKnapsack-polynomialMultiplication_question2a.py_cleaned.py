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
    items = iter(sorted(items, key=lambda t: t[2], reverse=True))
    selected_items = [0] * len(values)
    total_weight = 0
    while total_weight < capacity:
        try:
            item_idx, item_weight, _ = next(items)
            if total_weight + item_weight <= capacity:
                selected_items[item_idx - 1] = 1
                total_weight += item_weight
            else:
                selected_items[item_idx - 1] = (capacity - total_weight) / item_weight
                total_weight = capacity
        except StopIteration:
            break
    return [(i + 1, fraction) for i, fraction in enumerate(selected_items) if fraction > 0]
instance_path = "path_to_instance_file"
solve(instance_path)