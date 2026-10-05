
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
b1 = ReadGraph('b2.txt')
b2 = b1.read()
b3 = PlotGraph(b2)
b3.plot()