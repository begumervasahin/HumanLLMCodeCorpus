import sys
import random
input_data = []
SIGMA = 0.66
NO_OF_BOOTSTRAPS = int(sys.argv[1])
def bootstrapping(train_set):
    bootstrap = []
    num_instances = len(train_set)
    print("Number of Instances: %d" % num_instances)
    size_of_bootstrap = num_instances
    print("Size of One Bootstrap: %d" % size_of_bootstrap)
    for _ in range(NO_OF_BOOTSTRAPS):
        bootstrap_lst = [random.choice(train_set) for _ in range(size_of_bootstrap)]
        bootstrap.append(bootstrap_lst)
    for i, bootstrap_sample in enumerate(bootstrap):
        print("**********")
        print("Length of Bootstrap %d: %d" % (i+1, len(bootstrap_sample)))
def generate_train_test_samples(input_data):
    train_set = [line for line in input_data if random.random() < SIGMA]
    test_set = [line for line in input_data if random.random() >= SIGMA]
    print("Train Set:")
    print(train_set)
    print("Test Set:")
    print(test_set)
def main(input_data):
    generate_train_test_samples(input_data)
    bootstrapping(input_data)
if __name__ == "__main__":
    main(input_data)