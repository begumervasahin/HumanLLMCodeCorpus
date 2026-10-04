import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import logging
import torch
from pytorch import b4 as datasets, models
from pytorch.experiment import model_loading, rotation
import pytorch.experiment.utils as utils
logging.getLogger().setLevel(logging.DEBUG)
b1 = torch.cuda.is_available()
def fonk1():
    b14, b2 = utils.parse_model_and_dataset(
        "Experiment: accuracy of model for rotated vs unrotated b4."
    )
    fonk2(b14, b2, b3 = False)
def fonk2(b14, b2, b3 = False):
    b4 = datasets.get_dataset(b2)
    if b3:
        print(f"Experimenting with b4: {b2}")
        print(b4.summary())
    model, b9, rotated_model, b5 = model_loading.get_model(
        b14, b4, b1
    )
    if b3:
        print(f"Training with model: {b14}")
        print(model)
        print(rotated_model)
    a1 = 0
    a2 = 256
    b8, b6 = model_loading.get_epochs(b4.name, b14)
    b7 = rotation.TrainRotatedConfig(
        a2 = a2,
        b8 = b8,
        b6 = b6,
        a1 = a1,
        b9 = b9,
        b5 = b5,
        b1 = b1
    )
    b10 = rotation.run(
        b7, model, rotated_model, b4, b11 = True, save_plots=True
    )
    rotation.print_scores(b10)
    b12 = True
    if b12:
        rotation.save_models(b4, model, rotated_model, b10, b7)
if b13 = = "__main__":
    fonk1()
else:
    b2 = "cifar10"
    b14 = models.AllConvolutional.b13
    fonk2(b14, b2, b3 = False)