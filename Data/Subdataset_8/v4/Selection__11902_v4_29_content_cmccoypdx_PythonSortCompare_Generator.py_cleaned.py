import random
def generate_array(size):
    array = []
    for _ in range(size):
        array.append(random.randint(-size, size))
    return array
def generate_payload():
    payload = []
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    for size in sizes:
        payload.append(generate_array(size))
    return payload