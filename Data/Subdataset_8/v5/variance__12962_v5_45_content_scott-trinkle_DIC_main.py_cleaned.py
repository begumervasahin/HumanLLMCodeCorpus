
from dic.experiment import Experiment
from dic.plots import generate_plots
experiment_params = {
    'lens': 40,
    'weak_grad': False,
    'wavelength': 546,
    'approaches': ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
    'k_value': 1e2,
    'from_zero': True,
    'save_data': False,
    'filepath': None
}
experiment = Experiment(**experiment_params)
sigma_gamma, sigma_theta = experiment.generate_data(sample_size=100)
generate_plots(sigma_gamma, sigma_theta, experiment,
               polar=True,
               areaplot=True,
               snr=False,
               report=False,
               show=True)
