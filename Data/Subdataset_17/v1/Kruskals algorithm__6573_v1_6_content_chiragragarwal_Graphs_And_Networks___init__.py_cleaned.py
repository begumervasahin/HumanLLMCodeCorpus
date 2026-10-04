
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
if __name__ == "__main__":
    graph_reader = ReadGraph()
    graph = graph_reader.read('graph_data.txt')
    graph_plotter = PlotGraph()
    graph_plotter.plot(graph)