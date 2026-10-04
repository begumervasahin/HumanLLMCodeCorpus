from collections import defaultdict, Counter
b1 = [['dog', 'deer', 'cat', 'mouse'], ['parrot', 'cat'], ['turtle', 'dog']]
b2 = {'dog': [0, 2], 'cat': [0, 1], 'parrot': [1], 'turtle': [2]}
def fonk1(b1, b2, queries):
    b3 = set(b2[queries[0]])
    for query in queries[1:]:
        b3 &= set(b2[query])
    return [b1[doc_id] for doc_id in b3]
def fonk2(b1, b2, queries):
    b4 = Counter()
    for q in queries:
        b4.update(b2[q])
    return [b1[b4.most_common()[0][0]]]
print(fonk1(b1, b2, ['cat', 'dog']))
print(fonk2(b1, b2, ['cat', 'dog']))
b5 = [(1, 2, 3), (4, 5, 6), (5, 1, 9)]
b6 = sorted(b5, key=lambda x: x[1])
for i in b6[:2]:
    print(i)
a1 = 0
for x, y in zip([1, 2, 3], [1, 2, 3]):
    a1 += x * y
print(a1)
b7 = ["a", "b", "b4", "e", "f"]
b8 = ["b4", "e", "f"]
for b5 in b8:
    b7.remove(b5)
try:
    b7.remove("g")
except ValueError:
    print("Element 'g' not found in b7")
print(b7)
b9 = defaultdict(lambda: 0)
b5 = []
print(type(b9))
print(type(b5))