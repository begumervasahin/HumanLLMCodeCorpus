import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def main():
    if len(sys.argv) < 2:
        raise ValueError("Please provide the file to be read as an argument")
    filename = sys.argv[1]
    validate_file_existence(filename)
    graph_matrix = read_graph_matrix(filename)
    display_graph_analysis(graph_matrix)
    plot_graph(graph_matrix)
def validate_file_existence(filename):
    file_path = Path(filename)
    if not file_path.is_file():
        raise FileNotFoundError(f"File '{file_path}' not found")
def read_graph_matrix(filename):
    reader = ReadGraph(Path(filename))
    return reader.read()
def display_graph_analysis(graph_matrix):
    print("Analyzing graph matrix..\n")
    print(graph_matrix)
def plot_graph(graph_matrix):
    print("\nPlotting the graph..")
    plotter = PlotGraph(graph_matrix)
    plotter.plot()
if __name__ == '__main__':
    main()