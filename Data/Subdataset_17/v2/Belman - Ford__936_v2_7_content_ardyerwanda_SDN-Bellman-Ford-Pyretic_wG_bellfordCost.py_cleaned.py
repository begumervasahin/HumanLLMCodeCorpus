def abilene_cost_list():
    infinity = float('inf')
    num_nodes = 11
    route_table = {i: {j: {k: infinity for k in range(1, num_nodes + 1)} for j in range(1, num_nodes + 1)} for i in range(1, num_nodes + 1)}
    for i in range(1, num_nodes + 1):
        route_table[i][i][i] = 0
    costs = [
        (1, 2, 1), (1, 4, 1), (2, 3, 1), (2, 4, 1), (3, 6, 1),
        (4, 5, 1), (5, 6, 1), (5, 7, 1), (6, 11, 1), (7, 8, 1),
        (7, 11, 1), (8, 9, 1), (9, 10, 1), (10, 11, 1)
    ]
    for u, v, w in costs:
        route_table[u][u][v] = w
        route_table[v][v][u] = w
    return route_table
def main():
    route_table = abilene_cost_list()
    for router in route_table:
        print(f"Router {router}:")
        for src in route_table[router]:
            for dst in route_table[router][src]:
                if route_table[router][src][dst] < float('inf'):
                    print(f"  {src} -> {dst}: {route_table[router][src][dst]}")
if __name__ == "__main__":
    main()