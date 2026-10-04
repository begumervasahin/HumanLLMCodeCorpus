
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def main():
    graph_reader = ReadGraph()
    graph_file = 'graph_data.txt'
    graph = graph_reader.read(graph_file)
    graph_plotter = PlotGraph()
    graph_plotter.plot(graph)
if __name__ == "__main__":
    main()