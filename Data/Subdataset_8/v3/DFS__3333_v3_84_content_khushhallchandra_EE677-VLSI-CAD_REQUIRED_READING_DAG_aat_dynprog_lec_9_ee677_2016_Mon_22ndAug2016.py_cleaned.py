import copy
def topological_sort(fanin):
    topo_list = []
    while len(topo_list) < len(fanin):
        curr_node = find_node_without_fanin(fanin, topo_list)
        topo_list.append(curr_node)
        for v in range(len(fanin)):
            if curr_node in fanin[v]:
                fanin[v].remove(curr_node)
    return topo_list
def find_node_without_fanin(fanin, topo_list):
    for v in range(len(fanin)):
        if len(fanin[v]) == 0 and v not in topo_list:
            return v
    return None
def calculate_arrival_time(fanin, dly):
    aat = [0] * len(fanin)
    topo_sorted_nodes = topological_sort(copy.deepcopy(fanin))
    for node in topo_sorted_nodes:
        tmp = dly[node]
        for parent_node in fanin[node]:
            if tmp < aat[parent_node] + dly[node]:
                tmp = aat[parent_node] + dly[node]
        aat[node] = tmp
    return aat
fanin = [[3, 2, 1], [], [8, 5, 4, 3], [7, 6], [8, 6, 5], [7, 6], [9, 8], [9], [9], []]
dly = [10] * len(fanin)
print("Arrival time (aat) values are:", calculate_arrival_time(fanin, dly))