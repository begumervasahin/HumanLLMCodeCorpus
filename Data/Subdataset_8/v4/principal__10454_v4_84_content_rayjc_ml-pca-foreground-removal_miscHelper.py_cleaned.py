import argparse
import glob
import os
import numpy as np
imgDim = [120, 160]
class CliConfig:
    def __init__(self):
        self.config = self.get_cli_config()
        self.verify()
        self.process()
    @staticmethod
    def get_cli_config():
        main_parser = argparse.ArgumentParser(description="An application using L1 PCA to separate foreground and background by identifying moving parts.")
        sub_parsers = main_parser.add_subparsers(dest="subParser", help="Options: 'all' to preprocess frames and run PCA, 'preprocess' to only preprocess frames, 'train' to run PCA only")
        all_parser = sub_parsers.add_parser("all")
        process_parser = sub_parsers.add_parser("preprocess")
        for parser in (all_parser, process_parser):
            parser.add_argument("-i", "--input", default="input", type=str, help="Directory containing input frames (default: 'input')", metavar="input_dir")
            parser.add_argument("-o", "--output", default="unnamed", type=str, help="Name of output file excluding extension (default: 'unnamed')", metavar="output_name")
            parser.add_argument("-s", "--size", default=imgDim, type=int, nargs=2, help="Output resolution for all image frames (default: 120x160)", metavar=("img_height", "img_width"))
        all_parser.add_argument("-k", "--component", default=5, type=int, help="Number of principal components for PCA (default: 5)", metavar="component")
        all_parser.add_argument("-n", "--iteration", default=10, type=int, help="Number of gradient descent iterations for PCA (default: 10)", metavar="iteration")
        separate_parser = sub_parsers.add_parser("train")
        separate_parser.add_argument("-d", "--data", default="*.pkl", type=str, help="Input .pkl file containing a matrix of size nxd (n frames, d pixels) (default: searches current directory)", metavar="data_filepath")
        separate_parser.add_argument("-o", "--output", default="", type=str, help="Name of output file excluding extension (default: same as selected .pkl file)", metavar="output_name")
        separate_parser.add_argument("-s", "--size", default=imgDim, type=int, nargs=2, help="Image resolution of frames in .pkl (default: 120x160)", metavar=("img_height", "img_width"))
        separate_parser.add_argument("-k", "--component", default=5, type=int, help="Number of principal components for PCA (default: 5)", metavar="component")
        separate_parser.add_argument("-n", "--iteration", default=10, type=int, help="Number of gradient descent iterations for PCA (default: 10)", metavar="iteration")
        return vars(main_parser.parse_args())
    def process(self):
        self.config["size"] = tuple(self.config["size"])
        self.find_pickle_file()
    def verify(self):
        assert "." not in self.config["output"], "--output should not exclude any file extension"
        assert len(self.config["output"]) < 30, "--output should not exceed 30 characters"
        assert all(val < 3000 for val in self.config["size"]), "--size seems to be too large"
        if self.config["subParser"] in ["all", "preprocess"]:
            assert os.path.isdir(self.config["input"]), "Input directory does not exist"
        if self.config["subParser"] == "train":
            assert "pkl" in self.config["data"] and glob.glob(self.config["data"]), "Input data file must be in .pkl format"
    def find_pickle_file(self):
        if self.config["subParser"] == "train":
            matched_files = glob.glob(self.config["data"])
            if len(matched_files) > 1:
                data_file = input(f"Multiple .pkl files found: {matched_files}. Please enter one of the above: ")
                while data_file not in matched_files:
                    data_file = input(f"Multiple .pkl files found: {matched_files}. Please enter one of the above: ")
            else:
                data_file = matched_files[0]
            self.config["data"] = data_file
            self.config["output"] = os.path.splitext(data_file)[0]
def rgb2grey(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])