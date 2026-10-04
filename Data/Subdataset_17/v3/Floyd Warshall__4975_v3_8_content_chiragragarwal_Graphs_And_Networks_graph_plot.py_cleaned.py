import sys
from pathlib import Path
from read_graph import ReadGraph
from plot_graph import PlotGraph
def main(input_file):
    graph_reader = ReadGraph(input_file)
    graph_matrix = graph_reader.read()
    print("Analysing graph matrix...\n")
    print(graph_matrix)
    print("\nPlotting the graph...")
    graph_plotter = PlotGraph(graph_matrix)
    graph_plotter.plot()
if __name__ == '__main__':
    if len(sys.argv) <= 1:
        raise ValueError("Please enter the file to be read as an argument")
    input_file = Path(sys.argv[1])
    if not input_file.is_file():
        raise FileNotFoundError(f"The file {input_file} does not exist.")
    main(input_file)