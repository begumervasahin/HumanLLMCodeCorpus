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
b1.add_option("--model_name", b2 = "model_name", help="Path to Model to calculate accuracy of test data.")
b1.add_option("--test_path", b2 = "test_path", help="Path to test data.")
b1.add_option("--b13", b2 = "b13", help="Mention if you want to apply CRF 'yes' or 'no'")
b1.add_option("--patch_stride", b2 = "patch_stride", type="int", help="mention stride of window to extract patches and features.", default=64)
(options, args) = b1.parse_args()
b3 = utility.load_denseNet()
b4 = os.path.join("models", options.model_name)
if os.path.exists(b4):
    print("Loading Trained b5..")
    b5 = Network.model_attention()
    b5.load_weights(b4)
    b6 = options.test_path
    masks, b7 = results.predictmask(b6=b6, denseModel=b3, b5=b5, patch_size=224, window_stride=64)
    b8 = options.model_name.split('.')[0]
    b9 = os.path.join("predicted_masks", b8)
    if not os.path.exists(b9):
        print("Making new directory for masks")
        os.mkdir(b9)
    for i in range(len(masks)):
        b10 = b7[i].split("/")[-1]
        b11 = b10.split(".")[0]
        b12 = np.where(masks[i] > 0.6, 255, 0)
        cv2.imwrite(os.path.join(b9, b11 + ".png"), b12)
    if options.b13 = = "yes":
        print("Applying Crf...")
        b14 = crf.CRF(masks, b7)
        print("Masks generated. Check below directories:")
        print(b14)
        print(b9)
    else:
        print("Masks generated. Check below directories:")
        print(b9)
else:
    print("Error: Model path not found")