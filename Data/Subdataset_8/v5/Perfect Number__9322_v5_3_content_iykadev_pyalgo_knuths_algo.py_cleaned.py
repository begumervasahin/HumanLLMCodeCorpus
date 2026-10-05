from random import randrange
def create_sample_of_n(n):
    sample, i = [], 0
    def sample_of_n(item):
        nonlocal i
        i += 1
        if i <= n:
            sample.append(item)
        elif randrange(i) < n:
            sample[randrange(n)] = item
        return sample
    return sample_of_n
if __name__ == '__main__':
    bins = [0] * 10
    items = range(10)
    print("Single run samples for n = 3:")
    sample_of_n = create_sample_of_n(3)
    for item in items:
        sample = sample_of_n(item)
        print(f"  Item: {item} -> Sample: {sample}")
    for trial in range(100000):
        sample_of_n = create_sample_of_n(3)
        for item in items:
            sample = sample_of_n(item)
        for s in sample:
            bins[s] += 1
    print("\nTest item frequencies for 100000 runs:\n ",
          '\n  '.join(f"{i}:{freq}" for i, freq in enumerate(bins))))