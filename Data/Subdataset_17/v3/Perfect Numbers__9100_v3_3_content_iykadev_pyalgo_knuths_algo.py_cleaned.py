from random import randrange
def sample_of_n_creator(n):
    sample = []
    count = 0
    def sample_of_n(item):
        nonlocal count
        count += 1
        if count <= n:
            sample.append(item)
        elif randrange(count) < n:
            sample[randrange(n)] = item
        return sample
    return sample_of_n
if __name__ == '__main__':
    bin_counts = [0] * 10
    items = range(10)
    print("Single run samples for n = 3:")
    sample_of_n = sample_of_n_creator(3)
    for item in items:
        sample = sample_of_n(item)
        print(f"  Item: {item} -> sample: {sample}")
    num_trials = 100000
    for trial in range(num_trials):
        sample_of_n = sample_of_n_creator(3)
        for item in items:
            sample = sample_of_n(item)
        for s in sample:
            bin_counts[s] += 1
    print("\nTest item frequencies for 100000 runs:")
    for i, count in enumerate(bin_counts):
        print(f"  {i}: {count}")