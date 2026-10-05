
from dic.experiment import Experiment
from dic.plots import generate_plots
def main():
    experiment_config = {
        'lens': 40,
        'weak_grad': False,
        'lamda': 546,
        'approaches': ['A: 2x2', 'A: 2x3', 'B: 2x3', 'B: 2x4'],
        'k': 1e2,
        'fromZero': True,
        'save': False,
        'filepath': None
    }
    experiment = Experiment(**experiment_config)
    sample_size = 100
    sigma_g, sigma_t = experiment.generate_data(sample_size=sample_size)
    plot_options = {
        'polar': True,
        'areaplot': True,
        'SNR': False,
        'report': False,
        'show': True
    }
    generate_plots(sigma_g, sigma_t, experiment, **plot_options)
if __name__ == "__main__":
    main()