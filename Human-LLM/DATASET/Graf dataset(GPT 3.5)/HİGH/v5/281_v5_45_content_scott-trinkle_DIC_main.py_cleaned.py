
from dic.b2 import Experiment
from dic.plots import generate_plots
b1 = {
    'lens': 40,
    'weak_grad': False,
    'wavelength': 546,
    'approaches': ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
    'k_value': 1e2,
    'from_zero': True,
    'save_data': False,
    'filepath': None
}
b2 = Experiment(**b1)
sigma_gamma, b3 = b2.generate_data(sample_size=100)
generate_plots(sigma_gamma, b3, b2,
               b4 = True,
               b5 = True,
               b6 = False,
               b7 = False,
               b8 = True)
