import matplotlib as mpl
import matplotlib.pyplot as plt
import logging
from pytorch import b6 as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
logging.getLogger().setLevel(logging.DEBUG)
mpl.use('Agg')
plt.rcParams['image.cmap'] = 'gray'
b1 = "Accuracy vs rotation Experiment."
b2 = False
a1 = 16
b3 = "plots/accuracy_rotation"
model_name, b4 = utils.parse_model_and_dataset(b1)
b5 = torch.cuda.is_available()
b6 = datasets.get_dataset(b4)
if b2:
    print(b6.summary())
model, rotated_model, scores, b7 = rotation.load_models(b6, model_name, b5)
if b2:
    rotation.print_scores(scores)
rotated_results, classes, b8 = invariance_evaluation.run(rotated_model, b6, b7, a1)
results, b9, b9 = invariance_evaluation.run(model, b6, b7, a1)
b10 = invariance_evaluation.plot_results(rotated_results, classes, b8)
b11 = f"{b3}/{b6.name}b9{model.name}_rotated.png"
b10.savefig(b11)
b12 = invariance_evaluation.plot_results(results, classes, b8)
b13 = f"{b3}/{b6.name}b9{model.name}_unrotated.png"
b12.savefig(b13)