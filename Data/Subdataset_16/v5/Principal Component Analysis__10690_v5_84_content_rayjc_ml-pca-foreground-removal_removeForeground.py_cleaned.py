import pickle
import numpy as np
import miscHelper
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def fonk1(b7):
    b1 = createPklFile(b7.config["size"], b7.config["input"], b7.config["output"])
    print("Preprocess completed: image data has been compiled into", b1)
    return b1
def fonk2(file_name):
    with open(file_name, "rb") as f:
        b2 = pickle.load(f).astype(float) / 255
    return b2
def fonk3(b7, b2):
    b3 = b7.config["size"][0] * b7.config["size"][1]
    b4 = b2.shape[1]
    if b3 != b4:
        raise ValueError(
            f"The specified image resolution does not match data in .pkl file. "
            f"The default size is {miscHelper.imgDim[0]} by {miscHelper.imgDim[1]}. "
            "Otherwise, you may choose to specify the -s option."
        )
def fonk4(b7, b1 = None):
    if b7.config["subParser"] == "train":
        b2 = fonk2(b7.config["data"])
    else:
        b2 = fonk2(b1)
    fonk3(b7, b2)
    b5 = PCAL1(b7.config["component"], iteration=b7.config["iteration"])
    b6 = b5.fitTransform(b2, b7.config["size"])
    constructImageFrames(b2, b6, 0.1, b7.config["size"], b7.config["output"])
def fonk5():
    b7 = miscHelper.CliConfig()
    if b7.config["subParser"] in ("preprocess", "all"):
        b1 = fonk1(b7)
    else:
        b1 = None
    if b7.config["subParser"] in ("train", "all"):
        fonk4(b7, b1)
if b8 = = "__main__":
    fonk5()