import subprocess
import importlib
import sys
def install_and_import(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return importlib.import_module(package)
numpy = install_and_import("numpy")
from scipy.stats import norm
def calculate_historical_var(returns, confidence_level, time_period):
    alpha = 1 - (confidence_level / 100)
    var = -numpy.quantile(returns, alpha) * numpy.sqrt(time_period)
    return var
def calculate_var_covar(returns, confidence_level, time_period):
    alpha = 1 - (confidence_level / 100)
    std_dev = returns.std()
    mean = returns.mean()
    var = (norm.ppf(1 - alpha) * std_dev - mean) * numpy.sqrt(time_period)
    return var
def calculate_conditional_var_hist(returns, historical_var, time_period):
    cvar = -returns[returns < -historical_var / numpy.sqrt(time_period)].mean() * numpy.sqrt(time_period)
    return cvar
def calculate_conditional_var_covar(returns, confidence_level, time_period):
    alpha = 1 - (confidence_level / 100)
    std_dev = returns.std()
    mean = returns.mean()
    cvar = (alpha**-1 * norm.pdf(norm.ppf(alpha)) * std_dev - mean) * numpy.sqrt(time_period)
    return cvar