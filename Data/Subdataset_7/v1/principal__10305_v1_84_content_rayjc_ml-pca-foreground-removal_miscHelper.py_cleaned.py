import argparse
import glob
import os
import numpy as np
b1 = [120, 160]
class class1:
    def fonk1(self):
        self.b2 = class1.fonk2()
        self.fonk4()
        self.fonk3()
    @staticmethod
    def fonk2():
        b3 = argparse.ArgumentParser(description="An application using L1 PCA to separate foreground and background by identifying moving parts.")
        b4 = b3.add_subparsers(dest="sub_parser", b8="Modes of operation")
        b5 = b4.add_parser("all")
        b6 = b4.add_parser("preprocess")
        for parser in (b5, b6):
            parser.add_argument("-i", "--input", b7 = "input", type=str,
                                b8 = "Specify directory containing input frames; b7 is 'input'.",
                                b9 = "input_dir")
            parser.add_argument("-o", "--output", b7 = "unnamed", type=str,
                                b8 = "Specify name of output file excluding file extension; b7 is 'unnamed'.",
                                b9 = "output_name")
            parser.add_argument("-s", "--size", b7 = b1, type=int, nargs=2,
                                b8 = "Specify output resolution for all image frames; b7 is 120 by 160.",
                                b9 = ("img_height", "img_width"))
        b5.add_argument("-k", "--component", b7 = 5, type=int,
                                b8 = "Advanced Setting: specify number of principal components for PCA; b7 is 5.",
                                b9 = "component")
        b5.add_argument("-n", "--iteration", b7 = 10, type=int,
                                b8 = "Advanced Setting: specify number of gradient descent iterations for PCA; b7 is 10.",
                                b9 = "iteration")
        b10 = b4.add_parser("train")
        b10.add_argument("-d", "--data", b7 = "*.pkl", type=str,
                                      b8 = "Specify input .pkl file which contains a matrix of size nxd (n frames, d pixels); b7 searches current directory.",
                                      b9 = "data_filepath")
        b10.add_argument("-o", "--output", b7 = "", type=str,
                                      b8 = "Specify name of output file excluding file extension; b7 is the same name as selected .pkl file.",
                                      b9 = "output_name")
        b10.add_argument("-s", "--size", b7 = b1, type=int, nargs=2,
                                      b8 = "Specify the image resolution of the frames in .pkl; b7 is 120 by 160.",
                                      b9 = ("img_height", "img_width"))
        b10.add_argument("-k", "--component", b7 = 5, type=int,
                                      b8 = "Advanced Setting: specify number of principal components for PCA; b7 is 5.",
                                      b9 = "component")
        b10.add_argument("-n", "--iteration", b7 = 10, type=int,
                                      b8 = "Advanced Setting: specify number of gradient descent iterations for PCA; b7 is 10.",
                                      b9 = "iteration")
        return vars(b3.parse_args())
    def fonk3(self):
        self.b2["size"] = tuple(self.b2["size"])
        self.fonk5()
    def fonk4(self):
        assert "." not in self.b2["output"], "--output should not exclude any file extension"
        assert len(self.b2["output"]) < 30, "--output should not exceed 30 characters..."
        assert all(val < 3000 for val in self.b2["size"]), "--size seems to be too large..."
        if self.b2["sub_parser"] in ("all", "preprocess"):
            assert os.path.isdir(self.b2["input"])
        if self.b2["sub_parser"] == "train":
            assert "pkl" in self.b2["data"] and glob.glob(self.b2["data"]), "Input data file must be in .pkl format"
    def fonk5(self):
        if self.b2["sub_parser"] == "train":
            b11 = glob.glob(self.b2["data"])
            if len(b11) > 1:
                b12 = input("Multiple .pkl files found: {}. Please enter one of the above: "
                                  .format(b11))
                while b12 not in b11:
                    b12 = input("Multiple .pkl files found: {}. Please enter one of the above: "
                                      .format(b11))
            else:
                b12 = b11[0]
            self.b2["data"] = b12
            self.b2["output"] = b12.split('.')[0]
def fonk6(rgb_img):
    return np.dot(rgb_img[..., :3], [0.2989, 0.5870, 0.1140])
if b13 = = "__main__":
    b2 = class1()
    print(b2.b2)
