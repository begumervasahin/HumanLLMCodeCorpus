
from dic.experiment import Experiment
from dic.plots import generate_plots
experiment_params = {
    'lens': 40,
    'weak_grad': False,
    'lamda': 546,
    'approaches': ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
    'k': 1e2,
    'fromZero': True,
    'save': False,
    'filepath': None
}
experiment = Experiment(**experiment_params)
sigma_g, sigma_t = experiment.generate_data(sample_size=100)
generate_plots(sigma_g, sigma_t, experiment,
               polar=True,
               areaplot=True,
               SNR=False,
               report=False,
               show=True)
