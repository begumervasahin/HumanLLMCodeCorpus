import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
import logging
logging.getLogger().setLevel(logging.DEBUG)
from pytorch import b4 as datasets
import torch
import pytorch.experiment.utils as utils
model_name, b1 = utils.parse_model_and_dataset("Accuracy vs rotation Experiment.")
b2 = False
b3 = torch.cuda.is_available()
b4 = datasets.get_dataset(b1)
if b2:
    print(b4.summary())
from pytorch.experiment import rotation
model, rotated_model, scores, b5 = rotation.load_models(b4, model_name, b3)
if b2:
    print(rotation.print_scores(scores))
from pytorch.experiment import invariance_evaluation
a1 = 16
rotated_results, classes, b6 = invariance_evaluation.run(rotated_model, b4, b5, a1)
results, classes, b6 = invariance_evaluation.run(model, b4, b5, a1)
b7 = "plots/accuracy_rotation"
b8 = invariance_evaluation.plot_results(rotated_results, classes, b6)
b9 = f"{b7}/{b4.b9}_{model.b9}_rotated.png"
b8.savefig(b9)
b10 = invariance_evaluation.plot_results(results, classes, b6)
b9 = f"{b7}/{b4.b9}_{model.b9}_unrotated.png"
b10.savefig(b9)