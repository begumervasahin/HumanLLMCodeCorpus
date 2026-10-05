import argparse
import glob
import os
import numpy as np
imgDim = [120, 160]
class CliConfig:
    def __init__(self):
        self.config = CliConfig.get_cli_config()
        self.verify()
        self.process()
    @staticmethod
    def get_cli_config():
        main_parser = argparse.ArgumentParser(description="An application using L1 PCA to separate foreground and background by identifying moving parts.")
        sub_parsers = main_parser.add_subparsers(dest="sub_parser", help="Modes of operation")
        all_parser = sub_parsers.add_parser("all")
        process_parser = sub_parsers.add_parser("preprocess")
        for parser in (all_parser, process_parser):
            parser.add_argument("-i", "--input", default="input", type=str,
                                help="Specify directory containing input frames; default is 'input'.",
                                metavar="input_dir")
            parser.add_argument("-o", "--output", default="unnamed", type=str,
                                help="Specify name of output file excluding file extension; default is 'unnamed'.",
                                metavar="output_name")
            parser.add_argument("-s", "--size", default=imgDim, type=int, nargs=2,
                                help="Specify output resolution for all image frames; default is 120 by 160.",
                                metavar=("img_height", "img_width"))
        all_parser.add_argument("-k", "--component", default=5, type=int,
                                help="Advanced Setting: specify number of principal components for PCA; default is 5.",
                                metavar="component")
        all_parser.add_argument("-n", "--iteration", default=10, type=int,
                                help="Advanced Setting: specify number of gradient descent iterations for PCA; default is 10.",
                                metavar="iteration")
        separate_parser = sub_parsers.add_parser("train")
        separate_parser.add_argument("-d", "--data", default="*.pkl", type=str,
                                      help="Specify input .pkl file which contains a matrix of size nxd (n frames, d pixels); default searches current directory.",
                                      metavar="data_filepath")
        separate_parser.add_argument("-o", "--output", default="", type=str,
                                      help="Specify name of output file excluding file extension; default is the same name as selected .pkl file.",
                                      metavar="output_name")
        separate_parser.add_argument("-s", "--size", default=imgDim, type=int, nargs=2,
                                      help="Specify the image resolution of the frames in .pkl; default is 120 by 160.",
                                      metavar=("img_height", "img_width"))
        separate_parser.add_argument("-k", "--component", default=5, type=int,
                                      help="Advanced Setting: specify number of principal components for PCA; default is 5.",
                                      metavar="component")
        separate_parser.add_argument("-n", "--iteration", default=10, type=int,
                                      help="Advanced Setting: specify number of gradient descent iterations for PCA; default is 10.",
                                      metavar="iteration")
        return vars(main_parser.parse_args())
    def process(self):
        self.config["size"] = tuple(self.config["size"])
        self._find_pickle_file()
    def verify(self):
        assert "." not in self.config["output"], "--output should not exclude any file extension"
        assert len(self.config["output"]) < 30, "--output should not exceed 30 characters..."
        assert all(val < 3000 for val in self.config["size"]), "--size seems to be too large..."
        if self.config["sub_parser"] in ("all", "preprocess"):
            assert os.path.isdir(self.config["input"])
        if self.config["sub_parser"] == "train":
            assert "pkl" in self.config["data"] and glob.glob(self.config["data"]), "Input data file must be in .pkl format"
    def _find_pickle_file(self):
        if self.config["sub_parser"] == "train":
            matched_files = glob.glob(self.config["data"])
            if len(matched_files) > 1:
                data_file = input("Multiple .pkl files found: {}. Please enter one of the above: "
                                  .format(matched_files))
                while data_file not in matched_files:
                    data_file = input("Multiple .pkl files found: {}. Please enter one of the above: "
                                      .format(matched_files))
            else:
                data_file = matched_files[0]
            self.config["data"] = data_file
            self.config["output"] = data_file.split('.')[0]
def rgb2grey(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])
if __name__ == "__main__":
    config = CliConfig()
    print(config.config)
