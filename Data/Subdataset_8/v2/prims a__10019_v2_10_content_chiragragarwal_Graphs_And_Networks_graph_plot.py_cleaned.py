import sys
from pathlib import Path
from PlotGraph import PlotGraph
from ReadGraph import ReadGraph
if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError("Please provide the file to be read as an argument")
    filename = sys.argv[1]
    inputFile = Path(filename)
    if not inputFile.is_file():
        raise FileNotFoundError(f"File '{inputFile}' not found")
    reader = ReadGraph(inputFile)
    graphMat = reader.read()
    print("Analyzing graph matrix..\n")
    print(graphMat)
    print("\nPlotting the graph..")
    plotter = PlotGraph(graphMat)
    plotter.plot()