from pyspark import SparkContext
from pprint import pprint
def arrange_edges(edge):
    u, v, w = edge.split(' ')
    if float(w) < 0:
        return (u, [f"{v}:{w}"]), (v, []), (-1, [])
    return (u, [f"{v}:{w}"]), (v, [])
def gr_arrange_edges(edge):
    split_list = edge.split(' ')
    if split_list[0] != 'a':
        return []
    u, v, w = split_list[1], split_list[2], split_list[3]
    if int(w) < 0:
        return (u, [f"{v}:{w}"]), (v, []), (-1, [])
    return (u, [f"{v}:{w}"]), (v, [])
def get_negative_flag(it):
    for i in it:
        if i[0] == -1:
            return i
    return (None, None)
def get_graph(file_path, sc):
    data = sc.textFile(file_path, 8)
    if '.gr' in file_path:
        nodes_mapper = data.flatMap(gr_arrange_edges)
    else:
        nodes_mapper = data.flatMap(arrange_edges)
    flag_exist_negative = True if -1 in nodes_mapper.mapPartitions(get_negative_flag).collect() else False
    graph = nodes_mapper.reduceByKey(lambda x, y: x + y).filter(lambda x: x[0] != -1).sortByKey()
    return graph, flag_exist_negative
if __name__ == '__main__':
    sc = SparkContext.getOrCreate()
    graph, has_negative_weights = get_graph('data/input_slides.dat', sc)
    pprint(graph.collect())
    print(f"Contains negative weights: {has_negative_weights}")