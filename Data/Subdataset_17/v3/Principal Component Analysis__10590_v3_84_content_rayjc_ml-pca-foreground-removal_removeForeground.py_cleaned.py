import pickle
import numpy as np
from miscHelper import CliConfig, imgDim
from pca import PCAL1
from processFrames import constructImageFrames, createPklFile
def preprocess_data(size, input_path, output_path):
    pkl_file_name = createPklFile(size, input_path, output_path)
    print("Preprocess completed: image data has been compiled into", pkl_file_name)
    return pkl_file_name
def load_frame_data(pickle_file):
    with open(pickle_file, "rb") as f:
        frame_data = pickle.load(f).astype(float) / 255
    return frame_data
def validate_image_resolution(size, frame_data):
    assert size[0] * size[1] == frame_data.shape[1], (
        f"The specified image resolution does not match data in the .pkl file. "
        f"The default size is {imgDim[0]} by {imgDim[1]}. Otherwise, you may choose to specify the -s option."
    )
def train_model(frame_data, components, iterations, size):
    model = PCAL1(components, iteration=iterations)
    frame_data_new = model.fitTransform(frame_data, size)
    return frame_data_new
def main():
    cli = CliConfig()
    if cli.config["subParser"] in ("preprocess", "all"):
        pkl_file_name = preprocess_data(cli.config["size"], cli.config["input"], cli.config["output"])
    if cli.config["subParser"] in ("train", "all"):
        if cli.config["subParser"] == "train":
            frame_data = load_frame_data(cli.config["data"])
        else:
            frame_data = load_frame_data(pkl_file_name)
        validate_image_resolution(cli.config["size"], frame_data)
        frame_data_new = train_model(frame_data, cli.config["component"], cli.config["iteration"], cli.config["size"])
        constructImageFrames(frame_data, frame_data_new, 0.1, cli.config["size"], cli.config["output"])
if __name__ == "__main__":
    main()