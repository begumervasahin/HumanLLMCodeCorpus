from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def main():
    graph_file = 'graph_data.txt'
    graph_reader = ReadGraph(graph_file)
    graph_data = graph_reader.read()
    graph_plotter = PlotGraph(graph_data)
    graph_plotter.plot()
if __name__ == "__main__":
    main()