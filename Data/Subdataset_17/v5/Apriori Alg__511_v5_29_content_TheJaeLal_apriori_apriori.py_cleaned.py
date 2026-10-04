def read_from_file(fname):
    with open(fname, 'r') as file:
        dataset = file.read().split('\n')
    return [line.split(':')[1].split(',') for line in dataset if not (line.startswith('
def prune(item_set, threshold):
    return {item: count for item, count in item_set.items() if count >= threshold}
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
def initial_frequency_count(database):
    item_set = {}
    for entry in database:
        for item in entry:
            item = frozenset([item])
            if item in item_set:
                item_set[item] += 1
            else:
                item_set[item] = 1
    return item_set
def display_frequent_items(frequent_items):
    print('\n**** Frequent Items ****')
    for item in frequent_items:
        print(item)
def display_frequency_count(item_set):
    print('\n*** Frequency Count ***')
    for item, count in item_set.items():
        print(item, ':', count)
def display_initial_database(database):
    print("Initial Database:")
    for entry in database:
        print(entry)
def main():
    input_file = 'input.dat'
    database = read_from_file(input_file)
    database = [frozenset(entry) for entry in database]
    display_initial_database(database)
    item_set = initial_frequency_count(database)
    print('\n*** Initial Frequency Count ***')
    display_frequency_count(item_set)
    threshold = int(input('Enter Support Threshold: '))
    print('Threshold =', threshold)
    previous_item_set = item_set
    while True:
        frequent_items = prune(item_set, threshold)
        display_frequent_items(frequent_items)
        if len(frequent_items) < 1:
            frequent_items = previous_item_set
            break
        print("\n*** New Iteration ***")
        new_item_set = combine_sets(list(frequent_items.keys()))
        previous_item_set = frequent_items
        item_set = get_count(new_item_set, database)
        display_frequency_count(item_set)
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for item in frequent_items:
        print('{', ', '.join(item), '}')
    print('\n')
if __name__ == "__main__":
    main()