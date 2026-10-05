import sys
from path import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
if __name__ == '__main__':
    if not len(sys.argv) > 1:
        raise ValueError("Please provide the file to be read as an argument")
    inputFile = Path(sys.argv[1])
    graph_reader = ReadGraph(inputFile)
    graph_matrix = graph_reader.read()
    print("Analyzing graph matrix...\n")
    print(graph_matrix)
    print("\nPlotting the graph...")
    graph_plotter = PlotGraph(graph_matrix)
    graph_plotter.plot()