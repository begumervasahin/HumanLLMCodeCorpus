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
def single_run_demo(num_items, n):
    sampler = reservoir_sampler(n)
    for item in range(num_items):
        sample = sampler(item)
        print(f"  Item: {item} -> sample: {sample}")
def multiple_runs_demo(num_items, n, trials):
    frequency_bin = [0] * num_items
    for _ in range(trials):
        sampler = reservoir_sampler(n)
        for item in range(num_items):
            sampler(item)
        for sampled_item in sampler(0):
            frequency_bin[sampled_item] += 1
    return frequency_bin
def main():
    num_items = 10
    n = 3
    trials = 100000
    print("Single run samples for n = 3:")
    single_run_demo(num_items, n)
    frequency_bin = multiple_runs_demo(num_items, n, trials)
    print("\nTest item frequencies for 100000 runs:\n")
    for i, freq in enumerate(frequency_bin):
        print(f"  {i}: {freq}")
if __name__ == '__main__':
    main()