from __future__ import print_function, division
import CPUtimer
from data2 import instance_iterator, print_solution
def solve(instance_path):
    timer = CPUtimer.CPUTimer()
    for instance in instance_iterator(instance_path):
        instance_name, capacity, profits, weights = instance
        timer.reset()
        timer.start()
        for _ in range(2):
            items = knapsack(capacity, profits, weights)
            timer.lap()
        timer.stop()
        print_solution(profits, weights, items, instance_name, '2a', timer)
def knapsack(capacity, profits, weights):
    items = [(i + 1, w, p / w) for i, (p, w) in enumerate(zip(profits, weights))]
    items = sorted(items, key=lambda item: item[2], reverse=True)
    selected_items = [0] * len(profits)
    total_weight = 0
    for i, w, _ in items:
        if total_weight + w <= capacity:
            selected_items[i - 1] = 1
            total_weight += w
        else:
            selected_items[i - 1] = (capacity - total_weight) / w
            break
    return [(i + 1, fraction) for i, fraction in enumerate(selected_items) if fraction > 0]
if __name__ == "__main__":
    instance_path = 'path_to_instance_file'
    solve(instance_path)