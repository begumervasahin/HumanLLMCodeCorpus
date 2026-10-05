def prime_query(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of nodes and values are not equal")
    nodes = queries
    node_values = values
    pairs = list(zip(first, second))
    tree_dict = {}
    for index in range(1, n + 1):
        tree_dict[index] = []
    root_children = [x[1] if x.index(1) == 0 else x[0] for x in pairs if 1 in x]
    tree_dict[1] = root_children
    def create_tree_dict(index, dic, pairs_list):
        if index not in dic:
            return
        stack = dic[index][:]
        while stack:
            node = stack.pop()
            for idx, node_pairs in enumerate(pairs_list[:]):
                if node in node_pairs:
                    node_comp = node_pairs[1] if node_pairs.index(node) == 0 else node_pairs[0]
                    dic[node] = dic.get(node, []) + [node_comp]
                    del pairs_list[idx]
                    stack.append(node_comp)
        return dic
    tree = create_tree_dict(1, tree_dict, pairs.copy())
    def is_prime(x):
        if x < 2:
            return False
        if x in (2, 3, 5, 7):
            return True
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    def count_primes(node_dict, node, node_values):
        if node not in node_dict:
            return 0
        prime_counter = 1 if is_prime(node_values[node - 1]) else 0
        for child_node in node_dict[node]:
            prime_counter += count_primes(node_dict, child_node, node_values)
        return prime_counter
    primes_count = [count_primes(tree, node, node_values) for node in nodes]
    result = '\n'.join(map(str, primes_count))
    return result