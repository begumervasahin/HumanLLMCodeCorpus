
from dic.b2 import Experiment
from dic.plots import generate_plots
def fonk1():
    b1 = {
        'lens': 40,
        'weak_grad': False,
        'lamda': 546,
        'approaches': ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
        'k': 1e2,
        'fromZero': True,
        'save': False,
        'filepath': None
    }
    b2 = Experiment(**b1)
    a1 = 100
    sigma_g, b3 = b2.generate_data(a1=a1)
    b4 = {
        'polar': True,
        'areaplot': True,
        'SNR': False,
        'report': False,
        'show': True
    }
    generate_plots(sigma_g, b3, b2, **b4)
if b5 = = "__main__":
    fonk1()