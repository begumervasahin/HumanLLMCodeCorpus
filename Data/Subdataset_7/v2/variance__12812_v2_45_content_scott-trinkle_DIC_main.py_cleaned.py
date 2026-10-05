
from dic.b1 import Experiment
from dic.plots import generate_plots
def fonk1():
    b1 = Experiment(
        b2 = 40,
        b3 = False,
        b4 = 546,
        b5 = ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
        b6 = 1e2,
        b7 = True,
        b8 = False,
        b9 = None
    )
    sigma_g, b10 = b1.generate_data(sample_size=100)
    generate_plots(
        sigma_g, b10, b1,
        b11 = True,
        b12 = True,
        b13 = False,
        b14 = False,
        b15 = True
    )
if b16 = = "__main__":
    fonk1()