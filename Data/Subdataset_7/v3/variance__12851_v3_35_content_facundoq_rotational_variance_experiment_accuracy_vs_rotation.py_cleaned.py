import matplotlib.pyplot as plt
import logging
from pytorch import b6 as datasets
import torch
import pytorch.experiment.utils as utils
from pytorch.experiment import rotation, invariance_evaluation
def fonk1():
    logging.getLogger().setLevel(logging.DEBUG)
def fonk2():
    plt.rcParams['image.cmap'] = 'gray'
    mpl.use('Agg')
def fonk3():
    b1 = "Accuracy vs rotation Experiment."
    b2 = False
    a1 = 16
    b3 = "plots/accuracy_rotation"
    return b1, b2, a1, b3
def fonk4():
    model_name, b4 = utils.parse_model_and_dataset(b1)
    b5 = torch.cuda.is_available()
    b6 = datasets.get_dataset(b4)
    return model_name, b6, b5
def fonk5(model, rotated_model, b6, b14, a1):
    rotated_results, classes, b7 = invariance_evaluation.run(rotated_model, b6, b14, a1)
    results, b8, b8 = invariance_evaluation.run(model, b6, b14, a1)
    return rotated_results, results, classes, b7
def fonk6(rotated_results, results, classes, b7, b3, b4, model_name):
    b9 = invariance_evaluation.plot_results(rotated_results, classes, b7)
    b10 = f"{b3}/{b4}b8{model_name}_rotated.png"
    b9.savefig(b10)
    b11 = invariance_evaluation.plot_results(results, classes, b7)
    b12 = f"{b3}/{b4}b8{model_name}_unrotated.png"
    b11.savefig(b12)
if b13 = = "__main__":
    fonk1()
    fonk2()
    b1, b2, a1, b3 = fonk3()
    model_name, b6, b5 = fonk4()
    if b2:
        print(b6.summary())
    model, rotated_model, scores, b14 = rotation.load_models(b6, model_name, b5)
    if b2:
        rotation.print_scores(scores)
    rotated_results, results, classes, b7 = fonk5(model, rotated_model, b6, b14, a1)
    fonk6(rotated_results, results, classes, b7, b3, b6.name, model.name)