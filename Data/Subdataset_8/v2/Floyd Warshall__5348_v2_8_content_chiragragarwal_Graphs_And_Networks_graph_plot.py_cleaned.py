
import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def main():
    if len(sys.argv) <= 1:
        raise ValueError("Please enter the file to be read as an argument")
    input_file_path = Path(sys.argv[1])
    if not input_file_path.is_file():
        raise FileNotFoundError("File not found:", input_file_path)
    graph_reader = ReadGraph(input_file_path)
    graph_matrix = graph_reader.read()
    print("Analyzing the graph matrix...\n")
    print(graph_matrix)
    print("\nPlotting the graph...")
    graph_plotter = PlotGraph(graph_matrix)
    graph_plotter.plot()
if __name__ == '__main__':
    main()