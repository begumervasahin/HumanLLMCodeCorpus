import pickle
import numpy as np
from miscHelper import CliConfig, imgDim
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def main():
    cli = CliConfig()
    if cli.config["subParser"] in ("preprocess", "all"):
        pklFileName = createPklFile(cli.config["size"], cli.config["input"], cli.config["output"])
        print("Preprocess completed: image data has been compiled into", pklFileName)
    if cli.config["subParser"] in ("train", "all"):
        if cli.config["subParser"] == "train":
            with open(cli.config["data"], "rb") as f:
                frameData = pickle.load(f).astype(float) / 255
        else:
            with open(pklFileName, "rb") as f:
                frameData = pickle.load(f).astype(float) / 255
        assert cli.config["size"][0] * cli.config["size"][1] == frameData.shape[1], \
            .format(imgDim[0], imgDim[1])
        model = PCAL1(cli.config["component"], iteration=cli.config["iteration"])
        frameDataNew = model.fitTransform(frameData, cli.config["size"])
        constructImageFrames(frameData, frameDataNew, 0.1, cli.config["size"], cli.config["output"])
if __name__ == "__main__":
    main()