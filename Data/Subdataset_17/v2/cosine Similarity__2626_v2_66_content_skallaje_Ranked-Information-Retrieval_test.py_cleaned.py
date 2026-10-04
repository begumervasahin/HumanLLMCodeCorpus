from collections import defaultdict, Counter
documents = [['dog', 'deer', 'cat', 'mouse'], ['parrot', 'cat'], ['turtle', 'dog']]
index = {'dog': [0, 2], 'cat': [0, 1], 'parrot': [1], 'turtle': [2]}
def and_search1(documents, index, queries):
    if not queries:
        return []
    doc_ids = set(index.get(queries[0], []))
    for query in queries[1:]:
        doc_ids &= set(index.get(query, []))
    return [documents[doc_id] for doc_id in doc_ids]
def and_search2(documents, index, queries):
    c = Counter()
    for query in queries:
        c.update(index.get(query, []))
    most_common_doc_id = c.most_common(1)[0][0] if c else None
    return [documents[most_common_doc_id]] if most_common_doc_id is not None else []
print(and_search1(documents, index, ['cat', 'dog']))
print(and_search2(documents, index, ['cat', 'dog']))
tuples_list = [(1, 2, 3), (4, 5, 6), (5, 1, 9)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
for item in sorted_tuples[:2]:
    print(item)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
sum_of_products = sum(x * y for x, y in zip(list1, list2))
print(sum_of_products)
list1 = ["a", "b", "c", "e", "f"]
list2 = ["c", "e", "f"]
for element in list2:
    if element in list1:
        list1.remove(element)
try:
    list1.remove("g")
except ValueError:
    print("Element 'g' not found in list1")
print(list1)
default_dict = defaultdict(lambda: 0)
regular_list = []
print(type(default_dict))
print(type(regular_list))