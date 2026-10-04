def read_from_file(fname):
    with open(fname, 'r') as file:
        dataset = [
            line.split(':')[1].split(',')
            for line in file
            if not (line.startswith('
        ]
    return dataset
def prune(item_set, threshold):
    return [item for item in item_set if item_set[item] >= threshold]
def combine_sets(frequent_items):
    new_item_set = []
    for i in range(len(frequent_items)):
        for j in range(i + 1, len(frequent_items)):
            new_set = frequent_items[i].union(frequent_items[j])
            if new_set not in new_item_set:
                new_item_set.append(new_set)
    return new_item_set
def get_count(new_item_set, database):
    item_set = defaultdict(int)
    for item in new_item_set:
        for entry in database:
            if item.issubset(entry):
                item_set[item] += 1
    return item_set
def display_frequent_items(frequent_items, message):
    print(f'\n**** {message} ****')
    for item in frequent_items:
        print(f"{item}")
def main():
    input_file = 'input.dat'
    database = read_from_file(input_file)
    database = [frozenset(entry) for entry in database]
    print("Database Transactions:")
    for transaction in database:
        print(transaction)
    item_set = defaultdict(int)
    for transaction in database:
        for item in transaction:
            item_set[frozenset([item])] += 1
    display_frequent_items(item_set.items(), 'Initial Frequency Count')
    threshold = int(input('\nEnter Support Threshold:\n>>> '))
    print('Threshold =', threshold)
    previous_item_set = item_set
    while True:
        frequent_items = prune(item_set, threshold)
        display_frequent_items(frequent_items, 'Frequent Items')
        if not frequent_items:
            frequent_items = previous_item_set
            break
        print("\n*** New Iteration ***")
        new_item_set = combine_sets(frequent_items)
        previous_item_set = frequent_items
        item_set = get_count(new_item_set, database)
        display_frequent_items(item_set.items(), 'Frequency Count')
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for item in frequent_items:
        print(f"{{ {', '.join(item)} }}")
    print('\n')
if __name__ == "__main__":
    main()