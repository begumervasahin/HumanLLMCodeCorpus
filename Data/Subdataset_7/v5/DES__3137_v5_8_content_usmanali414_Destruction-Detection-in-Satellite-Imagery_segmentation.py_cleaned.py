from optparse import OptionParser
import os
import cv2
import numpy as np
import utility
import Network
import results
import crf
a1 = 0.6
def fonk1(model_name, test_path, b13):
    b1 = utility.load_denseNet()
    b2 = os.path.join("models", model_name)
    if os.path.exists(b2):
        print("Loading the trained b3...")
        b3 = Network.model_attention()
        b3.load_weights(b2)
        masks, b4 = results.predictmask(path_to_test=test_path,
                                                b5 = b1,
                                                b3 = b3,
                                                b6 = 224,
                                                b7 = 64)
        b8 = model_name.split('.')[0]
        b9 = os.path.join("predicted_masks", b8)
        if not os.path.exists(b9):
            print("Creating a new directory for masks")
            os.mkdir(b9)
        for i in range(len(masks)):
            b10 = b4[i].split("/")[-1]
            b11 = b10.split(".")[0]
            b12 = np.where(masks[i] > a1, 255, 0)
            cv2.imwrite(os.path.join(b9, b11 + ".png"), b12)
        if b13 = = "yes":
            print("Applying CRF...")
            b14 = crf.CRF(masks, b4)
            print("Masks generated. Check the directories below:")
            print(b14)
            print(b9)
        else:
            print("Masks generated. Check the directory below:")
            print(b9)
    else:
        print("Error: Model path not found")
if b15 = = "__main__":
    b16 = OptionParser()
    b16.add_option("--model_name", b17 = "model_name", help="Path to the b3 for calculating accuracy on test data.")
    b16.add_option("--test_path", b17 = "test_path", help="Path to the test data.")
    b16.add_option("--b13", b17 = "b13", help="Specify 'yes' or 'no' to apply CRF.")
    b16.add_option("--patch_stride", b17 = "patch_stride", type="int", help="Stride of window to extract patches and features.", default=64)
    (options, args) = b16.parse_args()
    fonk1(options.model_name, options.test_path, options.b13)