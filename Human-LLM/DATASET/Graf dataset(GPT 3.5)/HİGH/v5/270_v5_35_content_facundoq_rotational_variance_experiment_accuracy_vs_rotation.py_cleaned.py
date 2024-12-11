import matplotlib.pyplot as plt
import logging
import torch
from pytorch import b2 as datasets
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
plt.rcParams['image.cmap'] = 'gray'
def fonk1(name, b1 = False):
    if b1:
        b2 = datasets.get_dataset(name)
        print(b2.summary())
    return datasets.get_dataset(name)
def fonk2(model, b2, b8, a1):
    results, classes, b3 = invariance_evaluation.run(model, b2, b8, a1)
    return results, classes, b3
def fonk3(b12, folder, b7, model_name, rotation_type):
    b4 = f"{folder}/{b7}b9{model_name}b9{rotation_type}.png"
    b12.savefig(b4)
b5 = torch.cuda.is_available()
b6 = "Accuracy vs rotation Experiment."
model_name, b7 = utils.parse_model_and_dataset(b6)
b2 = fonk1(b7, b1)
model, rotated_model, scores, b8 = rotation.load_models(b7, model_name, b5)
if b1:
    rotation.print_scores(scores)
a1 = 16
rotated_results, classes, b3 = fonk2(rotated_model, b2, b8, a1)
results, b9, b9 = fonk2(model, b2, b8, a1)
b10 = "plots/accuracy_rotation"
b11 = invariance_evaluation.plot_results(rotated_results, classes, b3)
fonk3(b11, b10, b7, model_name, "rotated")
b12 = invariance_evaluation.plot_results(results, classes, b3)
fonk3(b12, b10, b7, model_name, "unrotated")