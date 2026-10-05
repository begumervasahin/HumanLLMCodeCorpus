import matplotlib.pyplot as plt
import logging
import torch
from pytorch import b4 as datasets
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
plt.rcParams['image.cmap'] = 'gray'
b1 = torch.cuda.is_available()
model_name, b2 = utils.parse_model_and_dataset("Accuracy vs rotation Experiment.")
b3 = False
if b3:
    b4 = datasets.get_dataset(b2)
    print(b4.summary())
model, rotated_model, scores, b5 = rotation.load_models(b2, model_name, b1)
if b3:
    rotation.print_scores(scores)
a1 = 16
rotated_results, classes, b6 = invariance_evaluation.run(rotated_model, b4, b5, a1)
results, b7, b7 = invariance_evaluation.run(model, b4, b5, a1)
b8 = "plots/accuracy_rotation"
b9 = invariance_evaluation.plot_results(rotated_results, classes, b6)
b10 = f"{b8}/{b2}b7{model_name}_rotated.png"
b9.savefig(b10)
b11 = invariance_evaluation.plot_results(results, classes, b6)
b12 = f"{b8}/{b2}b7{model_name}_unrotated.png"
b11.savefig(b12)