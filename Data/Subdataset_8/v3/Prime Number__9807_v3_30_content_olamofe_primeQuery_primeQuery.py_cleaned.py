def prime_query(n, first, second, values, queries):
    if n != len(values):
        raise ValueError("Number of nodes and values are not equal")
    adjacency_list = {}
    for index in range(1, n + 1):
        adjacency_list[index] = []
    for x, y in zip(first, second):
        adjacency_list[x].append(y)
        adjacency_list[y].append(x)
    def count_prime_nodes(node, visited, values):
        nonlocal prime_counter
        if node not in visited:
            visited.add(node)
            if is_prime(values[node - 1]):
                prime_counter += 1
            for neighbor in adjacency_list[node]:
                count_prime_nodes(neighbor, visited, values)
    def is_prime(x):
        if x < 2:
            return False
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True
    result = []
    for node in queries:
        prime_counter = 0
        visited = set()
        if node in adjacency_list:
            count_prime_nodes(node, visited, values)
        result.append(prime_counter)
    formatted_result = "\n".join(map(str, result))
    print(formatted_result)
    return formatted_result
n = 5
first = [1, 2, 2, 3, 3]
second = [2, 3, 4, 5, 6]
values = [10, 10, 10, 10, 10]
queries = [1, 2, 3, 4, 5]
prime_query(n, first, second, values, queries)