import random
from math import sqrt
n = 10000
numbers = list(range(n))
random.shuffle(numbers)
next_index = [-1] * n
for i in range(n - 1):
    next_index[numbers[i]] = numbers[i + 1]
head_index = numbers[0]
def search_element(x, start_index):
    steps = 0
    while x > numbers[start_index]:
        start_index = next_index[start_index]
        steps += 1
    return start_index, steps
def search_type_a(x):
    return search_element(x, head_index)
def search_type_b(x):
    start_index = head_index
    max_val = numbers[start_index]
    for j in range(int(sqrt(n))):
        current_val = numbers[j]
        if max_val < current_val <= x:
            start_index = j
            max_val = current_val
    return search_element(x, start_index)
def search_type_c(x):
    start_index = head_index
    max_val = numbers[start_index]
    for _ in range(int(sqrt(n))):
        random_index = random.randint(0, n - 1)
        random_val = numbers[random_index]
        if max_val < random_val <= x:
            start_index = random_index
            max_val = random_val
    return search_element(x, start_index)
def search_type_d(x):
    random_index = random.randint(0, n - 1)
    random_val = numbers[random_index]
    if x < random_val:
        return search_element(x, head_index)
    elif x > random_val:
        return search_element(x, next_index[random_index])
    else:
        return random_index, 0
steps_type_a = [search_type_a(random.randint(0, n - 1))[1] for _ in range(100)]
steps_type_b = [search_type_b(random.randint(0, n - 1))[1] for _ in range(100)]
steps_type_c = [search_type_c(random.randint(0, n - 1))[1] for _ in range(100)]
steps_type_d = [search_type_d(random.randint(0, n - 1))[1] for _ in range(100)]
print("Average Steps Type A:", sum(steps_type_a) / len(steps_type_a))
print("Average Steps Type B:", sum(steps_type_b) / len(steps_type_b))
print("Average Steps Type C:", sum(steps_type_c) / len(steps_type_c))
print("Average Steps Type D:", sum(steps_type_d) / len(steps_type_d))