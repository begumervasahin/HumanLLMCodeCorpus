import argparse
import cv2
import imutils
import numpy as np
from keras.models import load_model
from keras.preprocessing.image import img_to_array
def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--model", required=True, help="Path to the trained model")
    parser.add_argument("-i", "--image", required=True, help="Path to the input image")
    return parser.parse_args()
def preprocess_image(image):
    image_resized = cv2.resize(image, (28, 28))
    image_normalized = image_resized.astype("float") / 255.0
    return np.expand_dims(img_to_array(image_normalized), axis=0)
def load_trained_model(model_path):
    print("[INFO] Loading the network model...")
    return load_model(model_path)
def predict_image(image, model):
    aesthetic_score, not_aesthetic_score = model.predict(image)[0]
    label = "Aesthetic" if aesthetic_score > not_aesthetic_score else "Not Aesthetic"
    probability = aesthetic_score if aesthetic_score > not_aesthetic_score else not_aesthetic_score
    return label, probability
def add_label_to_image(image, label, probability):
    output_image = imutils.resize(image, width=400)
    cv2.putText(output_image, "{}: {:.2f}%".format(label, probability * 100), (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    return output_image
def main():
    args = parse_arguments()
    image = cv2.imread(args.image)
    processed_image = preprocess_image(image)
    model = load_trained_model(args.model)
    label, probability = predict_image(processed_image, model)
    output_image = add_label_to_image(image, label, probability)
    cv2.imshow("Output", output_image)
    cv2.waitKey(0)
if __name__ == "__main__":
    main()