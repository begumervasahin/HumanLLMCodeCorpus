def read_from_file(fname):
    with open(fname, 'r') as file:
        dataset = file.read().split('\n')
        dataset = [line.split(':')[1].split(',') for line in dataset if not (line.startswith('
    return dataset
def prune(item_set, threshold):
    return [item for item in item_set if item_set[item] >= threshold]
def combine_sets(frequent_items):
    new_item_set = []
    for i in range(len(frequent_items)):
        for j in range(i + 1, len(frequent_items)):
            new_set = frequent_items[i].union(frequent_items[j])
            new_item_set.append(new_set)
    return new_item_set
def get_count(new_item_set, database):
    item_set = {}
    for item in new_item_set:
        for entry in database:
            if item.issubset(entry):
                if item in item_set:
                    item_set[item] += 1
                else:
                    item_set[item] = 1
    return item_set
if __name__ == "__main__":
    input_file = 'input.dat'
    database = read_from_file(input_file)
    database = [frozenset(entry) for entry in database]
    for d in database:
        print(d)
    item_set = {}
    for entry in database:
        for item in entry:
            item = frozenset([item])
            if item in item_set:
                item_set[item] += 1
            else:
                item_set[item] = 1
    print('***Initial Frequency Count***')
    for item in item_set:
        print(item, ':', item_set[item])
    threshold = int(input('Enter Support Threshold:\n>>> '))
    print('threshold =', threshold)
    previous_item_set = item_set
    while True:
        frequent_items = prune(item_set, threshold)
        print('\n****Frequent Items****')
        for f in frequent_items:
            print(f)
        if len(frequent_items) < 1:
            frequent_items = previous_item_set
            break
        print("\n***New Iteration***")
        new_item_set = combine_sets(frequent_items)
        previous_item_set = frequent_items
        item_set = get_count(new_item_set, database)
        print('\n***Frequency Count***')
        for item in item_set:
            print(item, ':', item_set[item])
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for item in frequent_items:
        print('{', ', '.join(item), '}')
    print('\n')