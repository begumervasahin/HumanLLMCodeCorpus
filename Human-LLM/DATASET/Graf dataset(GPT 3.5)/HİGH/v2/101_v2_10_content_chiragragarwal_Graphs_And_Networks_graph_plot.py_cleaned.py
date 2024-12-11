import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
if b1 = = '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Please provide the file to be read as an argument")
    b2 = sys.argv[1]
    b3 = Path(b2)
    if not b3.is_file():
        raise FileNotFoundError(f"File '{b3}' not found")
    b4 = ReadGraph(b3)
    b5 = b4.read()
    print("Analyzing graph matrix..\n")
    print(b5)
    print("\nPlotting the graph..")
    b6 = PlotGraph(b5)
    b6.plot()