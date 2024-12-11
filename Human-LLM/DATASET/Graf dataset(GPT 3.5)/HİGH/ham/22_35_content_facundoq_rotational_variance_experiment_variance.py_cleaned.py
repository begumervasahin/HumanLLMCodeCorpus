import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['image.cmap'] = 'gray'
import logging
from pytorch import models
from pytorch import b6 as datasets
import torch
import pytorch.experiment.utils as utils
if b1 = = "__main__":
    b3,b2 = utils.parse_model_and_dataset("Experiment: accuracy of model for rotated vs unrotated b6.")
else:
    b2 = "cifar10"
    b3 = models.AllConvolutional.b1
print(f"
b4 = False
b5 = torch.cuda.is_available()
b6 = datasets.get_dataset(b2)
if b4:
    print(b6.summary())
from pytorch.experiment import rotation
model,rotated_model,scores,b7 = rotation.load_models(b6,b3,b5)
if b4:
    print("
    print("
    print("
    rotation.print_scores(scores)
from pytorch.experiment import variance
a1 = 16
b8 = "sum"
logging.info(f"Calculating measure with aggregation function {b8} for conv layers and {a1} rotations...")
b9 = variance.run_all(model,rotated_model,b6, b7, a1,b8,batch_size=64)
logging.info("Saving b9...")
variance.save_results(model.name,b6.name,b9,b8)