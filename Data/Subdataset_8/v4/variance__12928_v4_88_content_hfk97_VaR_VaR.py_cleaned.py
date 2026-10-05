import subprocess
import importlib
import sys
def get_package(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        return importlib.import_module(package)
numpy = get_package("numpy")
scipy = get_package("scipy")
from scipy.stats import norm
def historical_var(returns, confidence, days):
    alpha = (1 - (confidence / 100))
    var_hist = -numpy.quantile(returns, alpha)
    var_hist *= numpy.sqrt(days)
    return var_hist
def var_covar(returns, confidence, days):
    std_dev = returns.std()
    mean = returns.mean()
    alpha = (1 - (confidence / 100))
    var_var_covar = norm.ppf(1 - alpha) * std_dev - mean
    var_var_covar *= numpy.sqrt(days)
    return var_var_covar
def conditional_var_hist(returns, var_hist, days):
    var_hist /= numpy.sqrt(days)
    es_hist = -returns[returns < -var_hist].mean()
    es_hist *= numpy.sqrt(days)
    return es_hist
def conditional_var_covar(returns, confidence, days):
    alpha = (1 - (confidence / 100))
    std_dev = returns.std()
    mean = returns.mean()
    es_var_covar = alpha**-1 * norm.pdf(norm.ppf(alpha)) * std_dev - mean
    es_var_covar *= numpy.sqrt(days)
    return es_var_covar