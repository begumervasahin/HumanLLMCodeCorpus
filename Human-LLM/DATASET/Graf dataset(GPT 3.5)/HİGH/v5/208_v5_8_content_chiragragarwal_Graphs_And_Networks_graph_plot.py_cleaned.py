import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def fonk1():
    if len(sys.argv) <= 1:
        raise ValueError("Please provide the file path as a command-line argument")
    b1 = Path(sys.argv[1])
    if not b1.exists():
        raise FileNotFoundError("File not found:", b1)
    b2 = ReadGraph(b1)
    b3 = b2.read()
    print("Analyzing the graph matrix...\n")
    print(b3)
    print("\nPlotting the graph...")
    b4 = PlotGraph(b3)
    b4.plot()
if b5 = = '__main__':
    fonk1()