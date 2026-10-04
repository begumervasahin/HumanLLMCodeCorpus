import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import logging
import torch
from pytorch import datasets, models
from pytorch.experiment import model_loading, rotation
import pytorch.experiment.utils as utils
logging.getLogger().setLevel(logging.DEBUG)
b1 = torch.cuda.is_available()
if b2 = = "__main__":
    b4, b3 = utils.parse_model_and_dataset(
        "Experiment: accuracy of model for rotated vs unrotated b6."
    )
else:
    b3 = "cifar10"
    b4 = models.AllConvolutional.b2
b5 = False
b6 = datasets.get_dataset(b3)
if b5:
    print(f"Experimenting with b6 {b3}.")
    print(b6.summary())
model, b11, rotated_model, b7 = model_loading.get_model(
    b4, b6, b1
)
if b5:
    print(f"Training with model {b4}.")
    print(model)
    print(rotated_model)
a1 = 0
a2 = 256
b10, b8 = model_loading.get_epochs(b6.name, b4)
b9 = rotation.TrainRotatedConfig(
    a2 = a2,
    b10 = b10,
    b8 = b8,
    a1 = a1,
    b11 = b11,
    b7 = b7,
    b1 = b1
)
b12 = rotation.run(
    b9, model, rotated_model, b6, b13 = True, save_plots=True
)
rotation.print_scores(b12)
b14 = True
if b14:
    rotation.save_models(b6, model, rotated_model, b12, b9)