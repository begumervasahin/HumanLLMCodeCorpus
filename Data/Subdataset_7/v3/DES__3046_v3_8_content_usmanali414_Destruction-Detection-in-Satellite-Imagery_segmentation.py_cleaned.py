from optparse import OptionParser
import numpy as np
import cv2
import results
import Network
from imageio import imread, imsave
import crf
import utility
import os
b1 = OptionParser()
b1.add_option("--model_name", b2 = "model_name", help="Path to the b5 for calculating accuracy on test data.")
b1.add_option("--test_path", b2 = "test_path", help="Path to the test data.")
b1.add_option("--b15", b2 = "b15", help="Specify 'yes' or 'no' to apply CRF.")
b1.add_option("--patch_stride", b2 = "patch_stride", type="int", help="Stride of window to extract patches and features.", default=64)
(options, args) = b1.parse_args()
b3 = utility.load_denseNet()
b4 = os.path.join("models", options.model_name)
if os.path.exists(b4):
    print("Loading the trained b5...")
    b5 = Network.model_attention()
    b5.load_weights(b4)
    b6 = options.test_path
    masks, b7 = results.predictmask(
        b6 = b6,
        b8 = b3,
        b5 = b5,
        b9 = 224,
        a1 = 64
    )
    b10 = options.model_name.split('.')[0]
    b11 = os.path.join("predicted_masks", b10)
    if not os.path.exists(b11):
        print("Creating a new directory for masks")
        os.mkdir(b11)
    for i, mask in enumerate(masks):
        b12 = b7[i].split("/")[-1]
        b13 = b12.split(".")[0]
        b14 = np.where(mask > 0.6, 255, 0)
        cv2.imwrite(os.path.join(b11, b13 + ".png"), b14)
    if options.b15 = = "yes":
        print("Applying CRF...")
        b16 = crf.CRF(masks, b7)
        print("Masks generated. Check the directories below:")
        print(b16)
        print(b11)
    else:
        print("Masks generated. Check the directory below:")
        print(b11)
else:
    print("Error: Model path not found")