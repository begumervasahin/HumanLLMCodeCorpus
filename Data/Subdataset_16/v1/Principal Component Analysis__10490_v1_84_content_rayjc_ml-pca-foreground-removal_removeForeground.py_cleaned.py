import pickle
import numpy as np
from miscHelper import CliConfig, imgDim
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def fonk1():
    b1 = CliConfig()
    if b1.config["subParser"] in ("preprocess", "all"):
        b2 = createPklFile(b1.config["size"], b1.config["input"], b1.config["output"])
        print("Preprocess completed: image data has been compiled into", b2)
    if b1.config["subParser"] in ("train", "all"):
        if b1.config["subParser"] == "train":
            with open(b1.config["data"], "rb") as f:
                b3 = pickle.load(f).astype(float) / 255
        else:
            with open(b2, "rb") as f:
                b3 = pickle.load(f).astype(float) / 255
        assert b1.config["size"][0] * b1.config["size"][1] == b3.shape[1], \
            .format(imgDim[0], imgDim[1])
        b4 = PCAL1(b1.config["component"], iteration=b1.config["iteration"])
        b5 = b4.fitTransform(b3, b1.config["size"])
        constructImageFrames(b3, b5, 0.1, b1.config["size"], b1.config["output"])
if b6 = = "__main__":
    fonk1()