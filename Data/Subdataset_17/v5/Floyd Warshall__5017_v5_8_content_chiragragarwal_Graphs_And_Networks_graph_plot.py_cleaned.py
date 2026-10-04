import sys
from pathlib import Path
from plot_graph import PlotGraph
from read_graph import ReadGraph
def main(input_file_path):
    graph_reader = ReadGraph(input_file_path)
    graph_matrix = graph_reader.read()
    print("Analysing graph matrix...\n")
    print(graph_matrix)
    print("\nPlotting the graph...")
    graph_plotter = PlotGraph(graph_matrix)
    graph_plotter.plot()
if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise ValueError("Please provide exactly one argument: the path to the input file.")
    input_file_path = Path(sys.argv[1])
    if not input_file_path.is_file():
        raise FileNotFoundError(f"The file '{input_file_path}' does not exist.")
    main(input_file_path)