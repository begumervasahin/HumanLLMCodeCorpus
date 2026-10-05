from optparse import OptionParser
import os
import cv2
import numpy as np
import utility
import Network
import results
import crf
MASK_THRESHOLD = 0.6
def load_and_predict_masks(model_name, test_path, apply_CRF):
    model_densenet = utility.load_denseNet()
    modelpath = os.path.join("models", model_name)
    if os.path.exists(modelpath):
        print("Loading the trained model...")
        model = Network.model_attention()
        model.load_weights(modelpath)
        masks, nameslist = results.predictmask(path_to_test=test_path,
                                                denseModel=model_densenet,
                                                model=model,
                                                patch_size=224,
                                                window_stride=64)
        modelnamedir = model_name.split('.')[0]
        maskdir = os.path.join("predicted_masks", modelnamedir)
        if not os.path.exists(maskdir):
            print("Creating a new directory for masks")
            os.mkdir(maskdir)
        for i in range(len(masks)):
            imgname = nameslist[i].split("/")[-1]
            maskname = imgname.split(".")[0]
            mask = np.where(masks[i] > MASK_THRESHOLD, 255, 0)
            cv2.imwrite(os.path.join(maskdir, maskname + ".png"), mask)
        if apply_CRF == "yes":
            print("Applying CRF...")
            crfdir = crf.CRF(masks, nameslist)
            print("Masks generated. Check the directories below:")
            print(crfdir)
            print(maskdir)
        else:
            print("Masks generated. Check the directory below:")
            print(maskdir)
    else:
        print("Error: Model path not found")
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("--model_name", dest="model_name", help="Path to the model for calculating accuracy on test data.")
    parser.add_option("--test_path", dest="test_path", help="Path to the test data.")
    parser.add_option("--apply_CRF", dest="apply_CRF", help="Specify 'yes' or 'no' to apply CRF.")
    parser.add_option("--patch_stride", dest="patch_stride", type="int", help="Stride of window to extract patches and features.", default=64)
    (options, args) = parser.parse_args()
    load_and_predict_masks(options.model_name, options.test_path, options.apply_CRF)