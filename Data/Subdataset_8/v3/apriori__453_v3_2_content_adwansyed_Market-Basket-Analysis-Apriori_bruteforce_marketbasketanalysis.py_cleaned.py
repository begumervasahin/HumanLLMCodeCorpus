import time
def find_frequent_triples(dataset, min_support):
    triples_table = {}
    with open(dataset, 'r') as file:
        lines = file.readlines()
        for line in lines:
            items = sorted(line.split())
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    for k in range(j + 1, len(items)):
                        key = ','.join([items[i], items[j], items[k]])
                        triples_table[key] = triples_table.get(key, 0) + 1
        frequent_triples = [(value, key) for key, value in triples_table.items() if value > len(lines) * min_support]
        frequent_triples.sort(reverse=True)
        print_frequent_items(frequent_triples)
def find_frequent_doubles(dataset, min_support):
    pairs_table = {}
    with open(dataset, 'r') as file:
        lines = file.readlines()
        for line in lines:
            items = sorted(line.split())
            for i in range(len(items)):
                for j in range(i + 1, len(items)):
                    key = ','.join([items[i], items[j]])
                    pairs_table[key] = pairs_table.get(key, 0) + 1
        frequent_doubles = [(value, key) for key, value in pairs_table.items() if value > len(lines) * min_support]
        frequent_doubles.sort(reverse=True)
        print_frequent_items(frequent_doubles)
def print_frequent_items(frequent_items):
    for idx, (count, items) in enumerate(frequent_items, 1):
        print(f"{idx}) {items}: {count}")
if __name__ == "__main__":
    print('------------------------------------------------------------------------')
    print('Running...')
    print('Done!')
    min_support_threshold = 0.03
    dataset_file = 'movies.dat'
    print('------------------------------------------------------------------------')
    print('Running Frequent Doubles...')
    start_time = time.time()
    find_frequent_doubles(dataset_file, min_support_threshold)
    end_time = time.time()
    print('Time taken in seconds for frequent doubles:', end_time - start_time)
    print('Done!')
    print('------------------------------------------------------------------------')
    print('Running Frequent Triples...')
    start_time = time.time()
    find_frequent_triples(dataset_file, min_support_threshold)
    end_time = time.time()
    print('Time taken in seconds for frequent triples:', end_time - start_time)
    print('Done!')