import sys
import random
__author__ = 'Aniket'
inputData = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[3])
def perform_bootstrapping(train_set):
    bootstrap_samples = []
    size_of_bootstrap = len(train_set)
    print("Number of Instances:", len(train_set))
    print("One Bootstrap size:", size_of_bootstrap)
    for _ in range(NO_OF_BOOTSTRAPS):
        bootstrap_sample = [random.choice(train_set) for _ in range(size_of_bootstrap)]
        bootstrap_samples.append(bootstrap_sample)
    for i, sample in enumerate(bootstrap_samples):
        print("**********")
        print("Length of Sample", i + 1, ":", len(sample))
def generate_train_test_samples(input_data):
    train_set = []
    test_set = []
    for line in input_data:
        if random.random() < SIGMA:
            train_set.append(line)
        else:
            test_set.append(line)
    print("Train Set:")
    print(train_set)
    print("Test Set:")
    print(test_set)
    num_test_examples = len(test_set)
    return train_set, test_set, num_test_examples
def main(input_data):
    train_set, _, _ = generate_train_test_samples(input_data)
    perform_bootstrapping(train_set)
if __name__ == "__main__":
    main(inputData)