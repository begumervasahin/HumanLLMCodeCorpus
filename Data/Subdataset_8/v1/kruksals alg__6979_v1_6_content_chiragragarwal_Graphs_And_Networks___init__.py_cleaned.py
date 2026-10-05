from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
reader = ReadGraph('graph_data.txt')
graph_data = reader.read()
plotter = PlotGraph(graph_data)
plotter.plot()