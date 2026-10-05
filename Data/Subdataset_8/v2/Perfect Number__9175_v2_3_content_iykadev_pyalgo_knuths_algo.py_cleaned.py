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
    bin_counts = [0] * 10
    items = range(10)
    print("Single run samples for n = 3:")
    sample_creator = create_sample_of_n(3)
    for item in items:
        sample = sample_creator(item)
        print("  Item: %i -> Sample: %s" % (item, sample))
    for _ in range(100000):
        sample_creator = create_sample_of_n(3)
        for item in items:
            sample = sample_creator(item)
        for s in sample:
            bin_counts[s] += 1
    print("\nTest item frequencies for 100,000 runs:\n ",
          '\n  '.join("%i:%i" % x for x in enumerate(bin_counts)))