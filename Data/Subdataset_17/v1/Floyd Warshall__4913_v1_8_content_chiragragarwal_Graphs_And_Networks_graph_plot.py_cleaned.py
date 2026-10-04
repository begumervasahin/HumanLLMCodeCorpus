import sys
from pathlib import Path
from read_graph import ReadGraph
from plot_graph import PlotGraph
def main(input_file):
    r = ReadGraph(input_file)
    graph_matrix = r.read()
    print("Analysing graph matrix..\n")
    print(graph_matrix)
    print("\nPlotting the graph..")
    p = PlotGraph(graph_matrix)
    p.plot()
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise ValueError("Please enter the file to be read as an argument")
    input_file = Path(sys.argv[1])
    main(input_file)