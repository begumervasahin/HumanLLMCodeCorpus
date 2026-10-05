import sys
def redirect_io_to_files(input_file='apriori.txt', output_file='output.txt'):
    sys.stdin = open(input_file, 'r')
    sys.stdout = open(output_file, 'w')
def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i + 1, r):
            indices[j] = indices[j - 1] + 1
        yield tuple(pool[i] for i in indices)
def is_item_present(item, transaction):
    return item in transaction
def calculate_item_counts(items, transactions):
    counts = {}
    for i in range(1, len(items) + 1):
        com = combinations(items, i)
        for c in com:
            for j in range(0, len(transactions), 1):
                x = transactions[j].split()
                for i in c:
                    ans = is_item_present(i, x)
                    if not ans:
                        break
                if ans:
                    key = ','.join(c)
                    counts[key] = counts.get(key, 0) + 1
    return counts
def print_counts(new_dictionary):
    for item, count in new_dictionary.items():
        print(item, count)
        print(" ")
def statistics(counts_all, minimum_support):
    new_dictionary = {}
    highest_length = 0
    for item, count in counts_all.items():
        item = str(item).replace(',', '')
        new_dictionary[item] = count
        if new_dictionary[item] < minimum_support:
            del new_dictionary[item]
    print_counts(new_dictionary)
    for item, count in new_dictionary.items():
        if len(item) > highest_length:
            highest_length = len(item)
    last = highest_length
    while highest_length != 2:
        for item, count in new_dictionary.items():
            first = 0
            last = highest_length - 2
            if len(item) > highest_length - 2:
                x = len(item)
                while x >= highest_length - 2:
                    cal = new_dictionary[item] / new_dictionary[item[first:last]]
                    print(item[first:last], "=>", item, cal * 100, "% Chance")
                    print("")
                    first += 2
                    last += 2
                    x -= 2
        highest_length -= 2
def run():
    content = sys.stdin.readlines()
    transaction_count = int(content[0])
    minimum_support = int(content[-1])
    transactions = []
    items = []
    for i in range(1, transaction_count + 1, 1):
        transactions.append(content[i])
    for i in range(1, transaction_count + 1, 1):
        for line in content[i].split():
            if line not in items:
                items.append(line)
        items.sort()
    ans = calculate_item_counts(items, transactions)
    statistics(ans, minimum_support)
def main():
    redirect_io_to_files()
    run()
if __name__ == "__main__":
    main()