from random import randrange
def reservoir_sampler(n):
    sample = []
    count = 0
    def sample_item(item):
        nonlocal count
        count += 1
        if count <= n:
            sample.append(item)
        else:
            idx = randrange(count)
            if idx < n:
                sample[idx] = item
        return sample
    return sample_item
if __name__ == '__main__':
    num_items = 10
    n = 3
    trials = 100000
    frequency_bin = [0] * num_items
    items = range(num_items)
    print("Single run samples for n = 3:")
    sampler = reservoir_sampler(n)
    for item in items:
        sample = sampler(item)
        print(f"  Item: {item} -> sample: {sample}")
    for trial in range(trials):
        sampler = reservoir_sampler(n)
        for item in items:
            sample = sampler(item)
        for sampled_item in sample:
            frequency_bin[sampled_item] += 1
    print("\nTest item frequencies for 100000 runs:\n")
    print('\n'.join(f"  {i}:{freq}" for i, freq in enumerate(frequency_bin)))