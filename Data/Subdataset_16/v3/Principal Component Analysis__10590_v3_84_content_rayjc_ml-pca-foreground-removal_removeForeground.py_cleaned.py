import pickle
import numpy as np
from miscHelper import CliConfig, imgDim
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def fonk1(size, input_path, output_path):
    b1 = createPklFile(size, input_path, output_path)
    print("Preprocess completed: image data has been compiled into", b1)
    return b1
def fonk2(pickle_file):
    with open(pickle_file, "rb") as f:
        b2 = pickle.load(f).astype(float) / 255
    return b2
def fonk3(size, b2):
    assert size[0] * size[1] == b2.shape[1], (
        f"The specified image resolution does not match data in the .pkl file. "
        f"The default size is {imgDim[0]} by {imgDim[1]}. Otherwise, you may choose to specify the -s option."
    )
def fonk4(b2, components, iterations, size):
    b3 = PCAL1(components, iteration=iterations)
    b4 = b3.fitTransform(b2, size)
    return b4
def fonk5():
    b5 = CliConfig()
    if b5.config["subParser"] in ("preprocess", "all"):
        b1 = fonk1(b5.config["size"], b5.config["input"], b5.config["output"])
    if b5.config["subParser"] in ("train", "all"):
        if b5.config["subParser"] == "train":
            b2 = fonk2(b5.config["data"])
        else:
            b2 = fonk2(b1)
        fonk3(b5.config["size"], b2)
        b4 = fonk4(b2, b5.config["component"], b5.config["iteration"], b5.config["size"])
        constructImageFrames(b2, b4, 0.1, b5.config["size"], b5.config["output"])
if b6 = = "__main__":
    fonk5()