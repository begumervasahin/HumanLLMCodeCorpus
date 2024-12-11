import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
import logging
from pytorch import models
from pytorch import b6 as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, variance
def fonk1(description):
    return utils.fonk1(description)
def fonk2():
    return "cifar10", models.AllConvolutional.b2
def fonk3(b6):
    print(b6.summary())
def fonk4(model, rotated_model, b6, b8, a1, b9):
    logging.info(f"Calculating measure with aggregation function {b9} for conv layers and {a1} rotations...")
    b1 = variance.run_all(model, rotated_model, b6, b8, a1, b9, batch_size=64)
    logging.info("Saving b1...")
    variance.save_results(model.name, b6.name, b1, b9)
if b2 = = "__main__":
    b4, b3 = fonk1("Experiment: accuracy of model for rotated vs unrotated b6.")
    else:
        b3, b4 = fonk2()
    b5 = torch.cuda.is_available()
    b6 = datasets.get_dataset(b3)
    b7 = False
    if b7:
        fonk3(b6)
    model, rotated_model, scores, b8 = rotation.load_models(b6, b4, b5)
    if b7:
        print("\n" * 3)
        rotation.print_scores(scores)
    a1 = 16
    b9 = "sum"
    fonk4(model, rotated_model, b6, b8, a1, b9)