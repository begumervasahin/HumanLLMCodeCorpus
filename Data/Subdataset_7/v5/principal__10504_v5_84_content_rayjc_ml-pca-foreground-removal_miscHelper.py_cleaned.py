import argparse
import glob
import os
import numpy as np
b1 = [120, 160]
class class1:
    def fonk1(self):
        self.b2 = self.fonk2()
        self.fonk4()
        self.fonk3()
    @staticmethod
    def fonk2():
        b3 = argparse.ArgumentParser(description="An application using L1 PCA to separate foreground and background by identifying moving parts.")
        b4 = b3.add_subparsers(dest="subParser", help="Options: 'all' to preprocess frames and run PCA, 'preprocess' to only preprocess frames, 'train' to run PCA only")
        b5 = b4.add_parser("all")
        b6 = b4.add_parser("preprocess")
        for parser in (b5, b6):
            parser.add_argument("-i", "--input", b7 = "input", type=str, help="Directory containing input frames (b7: 'input')", metavar="input_dir")
            parser.add_argument("-o", "--output", b7 = "unnamed", type=str, help="Name of output file excluding extension (b7: 'unnamed')", metavar="output_name")
            parser.add_argument("-s", "--size", b7 = b1, type=int, nargs=2, help="Output resolution for all image frames (b7: 120x160)", metavar=("img_height", "img_width"))
        b5.add_argument("-k", "--component", b7 = 5, type=int, help="Number of principal components for PCA (b7: 5)", metavar="component")
        b5.add_argument("-n", "--iteration", b7 = 10, type=int, help="Number of gradient descent iterations for PCA (b7: 10)", metavar="iteration")
        b8 = b4.add_parser("train")
        b8.add_argument("-d", "--data", b7 = "*.pkl", type=str, help="Input .pkl file containing a matrix of size nxd (n frames, d pixels) (b7: searches current directory)", metavar="data_filepath")
        b8.add_argument("-o", "--output", b7 = "", type=str, help="Name of output file excluding extension (b7: same as selected .pkl file)", metavar="output_name")
        b8.add_argument("-s", "--size", b7 = b1, type=int, nargs=2, help="Image resolution of frames in .pkl (b7: 120x160)", metavar=("img_height", "img_width"))
        b8.add_argument("-k", "--component", b7 = 5, type=int, help="Number of principal components for PCA (b7: 5)", metavar="component")
        b8.add_argument("-n", "--iteration", b7 = 10, type=int, help="Number of gradient descent iterations for PCA (b7: 10)", metavar="iteration")
        return vars(b3.parse_args())
    def fonk3(self):
        self.b2["size"] = tuple(self.b2["size"])
        self.fonk5()
    def fonk4(self):
        assert "." not in self.b2["output"], "--output should not exclude any file extension"
        assert len(self.b2["output"]) < 30, "--output should not exceed 30 characters"
        assert all(val < 3000 for val in self.b2["size"]), "--size seems to be too large"
        if self.b2["subParser"] in ["all", "preprocess"]:
            assert os.path.isdir(self.b2["input"]), "Input directory does not exist"
        if self.b2["subParser"] == "train":
            assert "pkl" in self.b2["data"] and glob.glob(self.b2["data"]), "Input data file must be in .pkl format"
    def fonk5(self):
        if self.b2["subParser"] == "train":
            b9 = glob.glob(self.b2["data"])
            if len(b9) > 1:
                b10 = input(f"Multiple .pkl files found: {b9}. Please enter one of the above: ")
                while b10 not in b9:
                    b10 = input(f"Multiple .pkl files found: {b9}. Please enter one of the above: ")
            else:
                b10 = b9[0]
            self.b2["data"] = b10
            self.b2["output"] = os.path.splitext(b10)[0]
def fonk6(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])