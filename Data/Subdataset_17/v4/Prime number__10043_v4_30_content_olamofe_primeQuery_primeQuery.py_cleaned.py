def primeQuery(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of nodes and values are not equal")
    pairs = list(zip(first, second))
    tree = {i: [] for i in range(1, n + 1)}
    for x, y in pairs:
        tree[x].append(y)
        tree[y].append(x)
    def build_tree(root):
        visited = set()
        queue = [root]
        tree[root] = []
        while queue:
            node = queue.pop(0)
            visited.add(node)
            for neighbor in tree[node]:
                if neighbor not in visited:
                    tree[node].append(neighbor)
                    tree[neighbor].remove(node)
                    queue.append(neighbor)
        return tree
    tree = build_tree(1)
    def is_prime(x):
        if x <= 1:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    def count_primes_in_subtree(node, tree, values):
        count = 0
        stack = [node]
        while stack:
            current = stack.pop()
            if is_prime(values[current - 1]):
                count += 1
            stack.extend(tree[current])
        return count
    results = []
    for query in queries:
        results.append(count_primes_in_subtree(query, tree, values))
    return '\n'.join(map(str, results))
if __name__ == "__main__":
    n = 5
    first = [1, 1, 2, 3]
    second = [2, 3, 4, 5]
    values = [2, 3, 4, 5, 6]
    queries = [1, 2, 3]
    print(primeQuery(n, first, second, values, queries))