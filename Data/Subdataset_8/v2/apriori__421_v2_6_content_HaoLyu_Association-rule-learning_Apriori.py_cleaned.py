import sys
import time
import csv
from itertools import combinations
def join_prune(k):
    rt = {}
    if not any(k):
        return rt
    keys = list(k.keys())
    if len(keys) < 2:
        return rt
    leng = len(keys[0])
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            union = set(keys[i] + keys[j])
            if len(union) > leng + 1:
                continue
            new_key = tuple(sorted(union))
            if new_key not in rt:
                prune_yes = all(new_key[:m] + new_key[m + 1:] in k for m in range(len(new_key)))
                if prune_yes:
                    rt[new_key] = 0
    return rt
def join_set(k):
    rt = {}
    if not any(k):
        return rt
    keys = list(k.keys())
    if len(keys) < 2:
        return rt
    leng = len(keys[0])
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            union = set(keys[i] + keys[j])
            if len(union) > leng + 1:
                continue
            new_key = tuple(sorted(union))
            if new_key not in rt:
                rt[new_key] = 0
    return rt
def solution(data_file, result_file, sigma, row_size=0):
    matrix = []
    if row_size != 0:
        stop = 0
        with open(data_file) as file:
            for row in file:
                if stop == row_size:
                    break
                item = [int(one_item) for one_item in row.strip().split(' ') if one_item]
                if len(item) >= 3:
                    matrix.append(item)
                stop += 1
    else:
        with open(data_file) as file:
            for row in file:
                item = [int(one_item) for one_item in row.strip().split(' ') if one_item]
                if len(item) >= 3:
                    matrix.append(item)
    avg_row_length = 1 + sum(len(row) for row in matrix) / len(matrix)
    with open(result_file, 'w', newline='') as csvfile:
        fieldnames = ['set_size', 'frequency', 'items']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
    L1, C1 = {}, {}
    start_time = time.time()
    for transaction in matrix:
        for item in transaction:
            item_key = (item,)
            C1[item_key] = C1.get(item_key, 0) + 1
    for item, count in C1.items():
        if count >= sigma:
            L1[item] = count
    print("Round 1")
    print("1-item set length:", len(L1))
    Lk = L1
    Ck = {}
    del L1, C1
    k = 1
    skip_transactions = {}
    while Lk:
        k += 1
        print(f"Round {k}")
        if k <= 2:
            Ck = join_set(Lk)
        else:
            Ck = join_prune(Lk)
        Lk = {}
        if not Ck:
            break
        len_candidate = len(Ck)
        possible_group = 1
        for counter in range(k):
            possible_group *= avg_row_length
            avg_row_length -= 1
        if possible_group > 2 * len_candidate:
            for transaction_idx, transaction in enumerate(matrix):
                if transaction_idx in skip_transactions:
                    continue
                transaction_set = set(transaction)
                for one_candidate in Ck:
                    if set(one_candidate).issubset(transaction_set):
                        Ck[one_candidate] += 1
            for candidate, count in Ck.items():
                if count >= sigma:
                    Lk[candidate] = count
            del Ck
        else:
            for transaction_idx, transaction in enumerate(matrix):
                if transaction_idx in skip_transactions:
                    continue
                for one_candidate in combinations(transaction, k):
                    if one_candidate in Ck:
                        Ck[one_candidate] += 1
            for candidate, count in Ck.items():
                if count >= sigma:
                    Lk[candidate] = count
            del Ck
        for transaction_idx, transaction in enumerate(matrix):
            if transaction_idx in skip_transactions:
                continue
            transaction_set = set(transaction)
            if all(set(one_candidate).issubset(transaction_set) for one_candidate in Lk):
                skip_transactions[transaction_idx] = 1
        print(f"{k}-item frequent set length: {len(Lk)}")
        if k > 2:
            with open(result_file, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for key, value in Lk.items():
                    writer.writerow({'set_size': k,
                                     'frequency': value,
                                     'items': ' '.join(map(str, key))
                                     })
    print("--- %s seconds ---" % (time.time() - start_time))
if __name__ == '__main__':
    result_file = 'result.csv'
    sigma = 4
    row_size = 0
    data_file = 'input_file_example.dat'
    if len(sys.argv) > 2:
        try:
            data_file = sys.argv[1]
            result_file = sys.argv[2]
            sigma = int(sys.argv[3])
            row_size = int(sys.argv[4])
        except IndexError:
            pass
    solution(data_file, result_file, sigma, row_size)