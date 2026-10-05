from dic.b1 import Experiment
from dic.plots import generate_plots
def fonk1():
    b1 = Experiment(lens=40,
                            b2 = False,
                            b3 = 546,
                            b4 = ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
                            b5 = 1e2,
                            b6 = True,
                            b7 = False,
                            b8 = None)
    sigma_g, b9 = b1.generate_data(sample_size=100)
    generate_plots(sigma_g, b9, b1,
                   b10 = True,
                   b11 = True,
                   b12 = False,
                   b13 = False,
                   b14 = True)
if b15 = = "__main__":
    fonk1()