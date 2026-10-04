from collections import defaultdict, Counter
b1 = [['dog', 'deer', 'cat', 'mouse'], ['parrot', 'cat'], ['turtle', 'dog']]
b2 = {'dog': [0, 2], 'cat': [0, 1], 'parrot': [1], 'turtle': [2]}
def fonk1(b1, b2, queries):
    if not queries:
        return []
    b3 = set(b2.get(queries[0], []))
    for query in queries[1:]:
        b3 &= set(b2.get(query, []))
    return [b1[doc_id] for doc_id in b3]
def fonk2(b1, b2, queries):
    b4 = Counter()
    for query in queries:
        b4.update(b2.get(query, []))
    b5 = b4.most_common(1)[0][0] if b4 else None
    return [b1[b5]] if b5 is not None else []
print(fonk1(b1, b2, ['cat', 'dog']))
print(fonk2(b1, b2, ['cat', 'dog']))
b6 = [(1, 2, 3), (4, 5, 6), (5, 1, 9)]
b7 = sorted(b6, key=lambda x: x[1])
for item in b7[:2]:
    print(item)
b8 = [1, 2, 3]
b9 = [1, 2, 3]
b10 = sum(x * y for x, y in zip(b8, b9))
print(b10)
b8 = ["a", "b", "b4", "e", "f"]
b9 = ["b4", "e", "f"]
for element in b9:
    if element in b8:
        b8.remove(element)
try:
    b8.remove("g")
except ValueError:
    print("Element 'g' not found in b8")
print(b8)
b11 = defaultdict(lambda: 0)
b12 = []
print(type(b11))
print(type(b12))