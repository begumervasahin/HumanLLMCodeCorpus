import matplotlib.pyplot as plt
import logging
from pytorch import models, b4 as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, variance
logging.basicConfig(b1 = logging.INFO)
def fonk1():
    model_name, b2 = utils.parse_model_and_dataset("Experiment: accuracy of model for rotated vs unrotated b4.")
    b3 = torch.cuda.is_available()
    b4 = datasets.get_dataset(b2)
    model, rotated_model, scores, b5 = rotation.load_models(b4, model_name, b3)
    fonk2(model, rotated_model, b4, b5)
def fonk2(model, rotated_model, b4, b5):
    a1 = 16
    b6 = "sum"
    logging.info(f"Calculating measure with aggregation function {b6} for conv layers and {a1} rotations...")
    b7 = variance.run_all(model, rotated_model, b4, b5, a1, b6, batch_size=64)
    logging.info("Saving b7...")
    variance.save_results(model.name, b4.name, b7, b6)
if b8 = = "__main__":
    fonk1()