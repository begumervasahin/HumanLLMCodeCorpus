import copy
def topological_sort(fanin_copy):
    topo_list = []
    while len(topo_list) < len(fanin_copy):
        curr_src = find_node_without_fanin(fanin_copy, topo_list)
        topo_list.append(curr_src)
        for v in range(len(fanin_copy)):
            if curr_src in fanin_copy[v]:
                fanin_copy[v].remove(curr_src)
    return topo_list
def find_node_without_fanin(fanin_copy, topo_list):
    for v in range(len(fanin_copy)):
        if len(fanin_copy[v]) == 0 and v not in topo_list:
            return v
    return None
def calculate_aat_dynprog(fanin, dly):
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
print("Arrival After Time (AAT) values are:", calculate_aat_dynprog(fanin, dly))