
from dic.b2 import Experiment
from dic.plots import generate_plots
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
sigma_g, b3 = b2.generate_data(sample_size=100)
generate_plots(sigma_g, b3, b2,
               b4 = True,
               b5 = True,
               b6 = False,
               b7 = False,
               b8 = True)
