import sys
from pyspark import SparkContext
from data_operation import get_graph
from pyspark_dijkstra import Dijkstra
from pyspark_bellman_ford import Bellman_Ford
from pprint import pprint
def main():
    input_info = sys.argv
    input_len = len(input_info)
    if input_len < 2:
        raise ValueError('At least one input file (graph) is required')
    graph_path = input_info[1]
    sc = SparkContext.getOrCreate()
    print(f"Processing graph file: {graph_path}")
    graph, has_negative_weights = get_graph(graph_path, sc)
    if has_negative_weights:
        result = Bellman_Ford('1', graph, sc)
    else:
        result = Dijkstra('1', graph, sc)
    if input_len == 3:
        output_path = input_info[2]
        result.saveAsTextFile(output_path)
        print(f"Results saved to: {output_path}")
    else:
        pprint(result.collect())
if __name__ == '__main__':
    main()