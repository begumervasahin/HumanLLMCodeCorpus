def abilene_cost_list():
    infinity = float('inf')
    num_nodes = 11
    route_table = {
        i: {
            j: {k: infinity for k in range(1, num_nodes + 1)}
            for j in range(1, num_nodes + 1)
        }
        for i in range(1, num_nodes + 1)
    }
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
def print_routing_table(route_table):
    for router, table in route_table.items():
        print(f"Router {router}:")
        for src, destinations in table.items():
            for dst, cost in destinations.items():
                if cost < float('inf'):
                    print(f"  {src} -> {dst}: {cost}")
def main():
    route_table = abilene_cost_list()
    print_routing_table(route_table)
if __name__ == "__main__":
    main()