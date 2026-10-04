import pickle
import numpy as np
import miscHelper
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def preprocess(cli):
    pkl_file_name = createPklFile(cli.config["size"], cli.config["input"], cli.config["output"])
    print("Preprocess completed: image data has been compiled into", pkl_file_name)
    return pkl_file_name
def load_frame_data(file_name):
    with open(file_name, "rb") as f:
        frame_data = pickle.load(f).astype(float) / 255
    return frame_data
def validate_image_resolution(cli, frame_data):
    expected_size = cli.config["size"][0] * cli.config["size"][1]
    actual_size = frame_data.shape[1]
    if expected_size != actual_size:
        raise ValueError(
            f"The specified image resolution does not match data in .pkl file. "
            f"The default size is {miscHelper.imgDim[0]} by {miscHelper.imgDim[1]}. "
            "Otherwise, you may choose to specify the -s option."
        )
def train(cli, pkl_file_name=None):
    if cli.config["subParser"] == "train":
        frame_data = load_frame_data(cli.config["data"])
    else:
        frame_data = load_frame_data(pkl_file_name)
    validate_image_resolution(cli, frame_data)
    model = PCAL1(cli.config["component"], iteration=cli.config["iteration"])
    frame_data_new = model.fitTransform(frame_data, cli.config["size"])
    constructImageFrames(frame_data, frame_data_new, 0.1, cli.config["size"], cli.config["output"])
def main():
    cli = miscHelper.CliConfig()
    if cli.config["subParser"] in ("preprocess", "all"):
        pkl_file_name = preprocess(cli)
    else:
        pkl_file_name = None
    if cli.config["subParser"] in ("train", "all"):
        train(cli, pkl_file_name)
if __name__ == "__main__":
    main()