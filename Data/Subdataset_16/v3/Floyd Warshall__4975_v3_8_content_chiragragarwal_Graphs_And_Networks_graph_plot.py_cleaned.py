import sys
from pathlib import Path
from read_graph import ReadGraph
from plot_graph import PlotGraph
def fonk1(b5):
    b1 = ReadGraph(b5)
    b2 = b1.read()
    print("Analysing graph matrix...\n")
    print(b2)
    print("\nPlotting the graph...")
    b3 = PlotGraph(b2)
    b3.plot()
if b4 = = '__main__':
    if len(sys.argv) <= 1:
        raise ValueError("Please enter the file to be read as an argument")
    b5 = Path(sys.argv[1])
    if not b5.is_file():
        raise FileNotFoundError(f"The file {b5} does not exist.")
    fonk1(b5)