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
    b14, b2 = fonk2()
    fonk3(b14, b2, b3 = False)
def fonk2():
    return utils.parse_model_and_dataset(
        "Experiment: accuracy of model for rotated vs unrotated b4."
    )
def fonk3(b14, b2, b3 = False):
    b4 = fonk4(b2, b3)
    model, b10, rotated_model, b5 = fonk5(
        b14, b4, b3
    )
    b6 = fonk6(
        b4, b14, b10, b5
    )
    b7 = fonk7(b6, model, rotated_model, b4)
    fonk8(b7)
    fonk9(b4, model, rotated_model, b7, b6)
def fonk4(b2, b3):
    b4 = datasets.get_dataset(b2)
    if b3:
        print(f"Experimenting with b4: {b2}")
        print(b4.summary())
    return b4
def fonk5(b14, b4, b3):
    model, b10, rotated_model, b5 = model_loading.get_model(
        b14, b4, b1
    )
    if b3:
        print(f"Training with model: {b14}")
        print(model)
        print(rotated_model)
    return model, b10, rotated_model, b5
def fonk6(b4, b14, b10, b5):
    a1 = 0
    a2 = 256
    b9, b8 = model_loading.get_epochs(b4.name, b14)
    return rotation.TrainRotatedConfig(
        a2 = a2,
        b9 = b9,
        b8 = b8,
        a1 = a1,
        b10 = b10,
        b5 = b5,
        b1 = b1
    )
def fonk7(b6, model, rotated_model, b4):
    return rotation.run(
        b6, model, rotated_model, b4, b11 = True, save_plots=True
    )
def fonk8(b7):
    rotation.print_scores(b7)
def fonk9(b4, model, rotated_model, b7, b6):
    b12 = True
    if b12:
        rotation.save_models(b4, model, rotated_model, b7, b6)
if b13 = = "__main__":
    fonk1()
else:
    b2 = "cifar10"
    b14 = models.AllConvolutional.b13
    fonk3(b14, b2, b3 = False)