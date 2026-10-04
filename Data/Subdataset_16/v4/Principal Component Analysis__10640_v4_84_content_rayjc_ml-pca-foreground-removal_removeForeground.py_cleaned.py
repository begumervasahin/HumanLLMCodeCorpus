import pickle
import numpy as np
import miscHelper
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def fonk1(b5):
    b1 = createPklFile(b5.config["size"], b5.config["input"], b5.config["output"])
    print("Preprocess completed: image data has been compiled into", b1)
    return b1
def fonk2(file_name, size):
    with open(file_name, "rb") as f:
        b2 = pickle.load(f).astype(float) / 255
    return b2
def fonk3(b5, b1 = None):
    if b5.config["subParser"] == "train":
        b2 = fonk2(b5.config["data"], b5.config["size"])
    else:
        b2 = fonk2(b1, b5.config["size"])
    assert b5.config["size"][0] * b5.config["size"][1] == b2.shape[1], \
        f"The specified image resolution does not match data in .pkl file. The default size is {miscHelper.imgDim[0]} by {miscHelper.imgDim[1]}. Otherwise, you may choose to specify the -s option."
    b3 = PCAL1(b5.config["component"], iteration=b5.config["iteration"])
    b4 = b3.fitTransform(b2, b5.config["size"])
    constructImageFrames(b2, b4, 0.1, b5.config["size"], b5.config["output"])
def fonk4():
    b5 = miscHelper.CliConfig()
    if b5.config["subParser"] in ("preprocess", "all"):
        b1 = fonk1(b5)
    else:
        b1 = None
    if b5.config["subParser"] in ("train", "all"):
        fonk3(b5, b1)
if b6 = = "__main__":
    fonk4()