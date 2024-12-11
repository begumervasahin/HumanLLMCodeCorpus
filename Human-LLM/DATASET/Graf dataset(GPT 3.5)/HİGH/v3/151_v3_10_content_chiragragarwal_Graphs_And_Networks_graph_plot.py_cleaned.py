import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
def fonk1():
    if len(sys.argv) < 2:
        raise ValueError("Please provide the file to be read as an argument")
    b1 = sys.argv[1]
    fonk2(b1)
    b2 = fonk3(b1)
    fonk4(b2)
    fonk5(b2)
def fonk2(b1):
    b3 = Path(b1)
    if not b3.is_file():
        raise FileNotFoundError(f"File '{b3}' not found")
def fonk3(b1):
    b4 = ReadGraph(Path(b1))
    return b4.read()
def fonk4(b2):
    print("Analyzing graph matrix..\n")
    print(b2)
def fonk5(b2):
    print("\nPlotting the graph..")
    b5 = PlotGraph(b2)
    b5.plot()
if b6 = = '__main__':
    fonk1()