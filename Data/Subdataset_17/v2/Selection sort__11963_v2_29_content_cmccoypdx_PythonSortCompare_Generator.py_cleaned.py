import random
def generate_array(size):
    return [random.randint(-size, size) for _ in range(size)]
def generate_payload():
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    return [generate_array(size) for size in sizes]
payload = generate_payload()
for index, array in enumerate(payload):
    print(f"Array {index + 1} size: {len(array)}")