from itertools import combinations
def readFile(filename):
    results = []
    with open(filename, 'r') as fData:
        for line in fData:
            results.append(line.strip())
    return results
def singleCandidates(dataset):
    results = []
    for transaction in dataset:
        items = transaction.split(',')
        for item in items:
            if item not in results:
                results.append(item)
    return results
def countCandidates(dataset, singles):
    candidateCount = {}
    for transaction in dataset:
        items = transaction.split(',')
        for item in items:
            for candidate in singles:
                if candidate == item:
                    candidateCount.setdefault(candidate, 0)
                    candidateCount[candidate] += 1
    return candidateCount
def totalItems(dataset):
    total = 0
    for transaction in dataset:
        items = transaction.split(',')
        total += len(items)
    return total
def supportCheck(itemCount, candidateCount, support):
    supportNumbers = {}
    for candidate in candidateCount:
        if candidateCount[candidate] / itemCount >= support:
            supportNumbers[candidate] = candidateCount[candidate] / itemCount
    return supportNumbers
def supportCheckCount(itemCount, candidateCount, support):
    result = []
    for candidate in candidateCount:
        if candidateCount[candidate] / itemCount >= support:
            result.append(candidate)
    return result
def frequentPairs(frequentItems, dataset, itemCount, support):
    results = {}
    for transaction in dataset:
        items = transaction.split(',')
        for item in combinations(items, 2):
            results.setdefault(item, 0)
            results[item] += 1
    markForDeletion = []
    for key in results:
        if results[key] / itemCount < support:
            markForDeletion.append(key)
        else:
            results[key] = results[key] / itemCount
    for key in markForDeletion:
        results.pop(key, None)
    return results
if __name__ == "__main__":
    dataFile = 'mushroom.data'
    support = 0.03
    data = readFile(dataFile)
    candidates1 = singleCandidates(data)
    print("Single item candidates:", candidates1)
    counts = countCandidates(data, candidates1)
    print("Counts of single item candidates:", counts)
    total = totalItems(data)
    print("Total number of items:", total)
    frequentCandidates = supportCheck(total, counts, support)
    print("Frequent single item candidates:", frequentCandidates)
    supportCounts = supportCheckCount(total, counts, support)
    print("Frequent single item candidates (counts):", supportCounts)
    pairs = frequentPairs(supportCounts, data, total, support)
    print("Frequent pairs:")
    for pair in pairs:
        print(f"{pair}: {pairs[pair]}")
    print("Time taken:", time.time() - start_time)