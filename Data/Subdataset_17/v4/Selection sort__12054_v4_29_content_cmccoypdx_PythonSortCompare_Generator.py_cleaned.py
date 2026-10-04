import random
def generate_array(size):
    return [random.randint(-size, size) for _ in range(size)]
def generate_payload():
    sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    payload = [generate_array(size) for size in sizes]
    return payload
if __name__ == "__main__":
    payload = generate_payload()
    for i, arr in enumerate(payload):
        print(f"Array of size {len(arr)}: {arr[:10]}...")
