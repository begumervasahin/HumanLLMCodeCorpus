
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
graph_reader = ReadGraph('graph_data.txt')
graph_data = graph_reader.read()
graph_plotter = PlotGraph(graph_data)
graph_plotter.plot()