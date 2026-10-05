import sys
import random
import KNN
input_data = []
sigma = 0.66
num_bootstraps = int(sys.argv[2])
def bootstrap(train_set):
    global bootstrap_samples
    bootstrap_samples = []
    print("Number of instances: %d" % len(train_set))
    bootstrap_size = int(len(train_set) / num_bootstraps)
    print("Size of each bootstrap sample: %d" % bootstrap_size)
    for _ in range(num_bootstraps):
        bootstrap_lst = []
        for _ in range(bootstrap_size):
            bootstrap_lst.append(random.choice(train_set))
        bootstrap_samples.append(bootstrap_lst)
    for i, sample in enumerate(bootstrap_samples):
        print("**********")
        print("Length of bootstrap sample %d: %d" % (i+1, len(sample)))
def generate_train_test_samples(input_file):
    fin = open(input_file, "r")
    global train_set, test_set
    train_set, test_set = [], []
    for line in fin:
        new_line = line.strip().split(',')
        data_set = train_set if random.random() < sigma else test_set
        data_set.append(new_line)
def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py <input_file> <number_of_bootstraps>")
        sys.exit(1)
    input_file = sys.argv[1]
    global train_set, test_set, bootstrap_samples
    generate_train_test_samples(input_file)
    bootstrap(train_set)
    KNN.main(bootstrap_samples[1], test_set, 3)
if __name__ == "__main__":
    main()