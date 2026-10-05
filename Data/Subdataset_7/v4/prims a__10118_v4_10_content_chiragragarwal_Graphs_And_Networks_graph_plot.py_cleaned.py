import sys
from path import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
if b1 = = '__main__':
    if not len(sys.argv) > 1:
        raise ValueError("Please provide the file to be read as an argument")
    b2 = Path(sys.argv[1])
    b3 = ReadGraph(b2)
    b4 = b3.read()
    print("Analyzing graph matrix...\n")
    print(b4)
    print("\nPlotting the graph...")
    b5 = PlotGraph(b4)
    b5.plot()