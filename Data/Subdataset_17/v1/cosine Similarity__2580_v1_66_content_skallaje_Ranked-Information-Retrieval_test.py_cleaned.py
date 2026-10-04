from collections import defaultdict, Counter
documents = [['dog', 'deer', 'cat', 'mouse'], ['parrot', 'cat'], ['turtle', 'dog']]
index = {'dog': [0, 2], 'cat': [0, 1], 'parrot': [1], 'turtle': [2]}
def and_search1(documents, index, queries):
    doc_ids = set(index[queries[0]])
    for query in queries[1:]:
        doc_ids &= set(index[query])
    return [documents[doc_id] for doc_id in doc_ids]
def and_search2(documents, index, queries):
    c = Counter()
    for q in queries:
        c.update(index[q])
    return [documents[c.most_common()[0][0]]]
print(and_search1(documents, index, ['cat', 'dog']))
print(and_search2(documents, index, ['cat', 'dog']))
l = [(1, 2, 3), (4, 5, 6), (5, 1, 9)]
fn = sorted(l, key=lambda x: x[1])
for i in fn[:2]:
    print(i)
sum_val = 0
for x, y in zip([1, 2, 3], [1, 2, 3]):
    sum_val += x * y
print(sum_val)
l1 = ["a", "b", "c", "e", "f"]
l2 = ["c", "e", "f"]
for l in l2:
    l1.remove(l)
try:
    l1.remove("g")
except ValueError:
    print("Element 'g' not found in l1")
print(l1)
d = defaultdict(lambda: 0)
l = []
print(type(d))
print(type(l))