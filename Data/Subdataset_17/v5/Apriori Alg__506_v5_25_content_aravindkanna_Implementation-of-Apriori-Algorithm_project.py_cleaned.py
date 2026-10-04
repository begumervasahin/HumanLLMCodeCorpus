import sys
import time
import fileinput
from math import ceil
from Trie import trieNode
from otherMethods import generate, prune, item_sets_count, print_associate_rules
start = time.time()
params = {}
with open('config.csv') as conf:
    for line in conf:
        key, value = line.strip().split(",")
        params[key] = value
in_file = params["input"]
out_file = params["output"]
flag = int(params["flag"])
min_support = float(params["support"])
min_confidence = float(params["confidence"])
sys.stdout = open(out_file, 'w')
singletons = {}
num_transactions = 0
with open(in_file) as infp:
    for line in infp:
        items = line.strip().split(",")
        for item in items:
            singletons[item] = singletons.get(item, 0) + 1
        num_transactions += 1
min_transactions = ceil(num_transactions * min_support)
frequent_singles = []
frequent_singles_count = []
print("FreqCount")
for item, count in singletons.items():
    if count >= min_transactions:
        print(item)
        frequent_singles.append([item])
        frequent_singles_count.append(count)
frequent_singles.sort()
freqs_trie = trieNode()
freqs_trie.insertAll(frequent_singles, frequent_singles_count)
freq_item_sets = frequent_singles
current_size_list = frequent_singles
total_freqs = len(current_size_list)
while True:
    next_size_list = generate(current_size_list)
    pruned_list = prune(freqs_trie, next_size_list)
    if not pruned_list:
        break
    counts = item_sets_count(in_file, pruned_list)
    frequent_items = []
    frequent_counts = []
    for i, candidate in enumerate(pruned_list):
        if counts[i] >= min_transactions:
            print(",".join(candidate))
            frequent_items.append(candidate)
            frequent_counts.append(counts[i])
    if not frequent_counts:
        break
    freqs_trie.insertAll(frequent_items, frequent_counts)
    current_size_list = frequent_items
    total_freqs += len(current_size_list)
if flag == 1:
    print("RulesCount")
    num_rules = print_associate_rules(freqs_trie, min_confidence)
sys.stdout.close()
for line in fileinput.input(out_file, inplace=True):
    if "RulesCount" in line and flag == 1:
        line = line.replace(line, str(num_rules) + "\n")
    elif "FreqCount" in line:
        line = line.replace(line, str(total_freqs) + "\n")
    print(line, end='')
