import subprocess
import importlib
import sys
def get_package(package_name):
    try:
        return importlib.import_module(package_name)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return importlib.import_module(package_name)
np = get_package("numpy")
from scipy.stats import norm
def var_hist(returns, confidence_level, days):
    alpha = 1 - (confidence_level / 100)
    var = -np.quantile(returns, alpha) * np.sqrt(days)
    return var
def var_vcov(returns, confidence_level, days):
    alpha = 1 - (confidence_level / 100)
    std_dev = np.std(returns)
    mean = np.mean(returns)
    var = (norm.ppf(1 - alpha) * std_dev - mean) * np.sqrt(days)
    return var
def cvar_hist(returns, var, days):
    es = -returns[returns < -var / np.sqrt(days)].mean() * np.sqrt(days)
    return es
def cvar_vcov(returns, confidence_level, days):
    alpha = 1 - (confidence_level / 100)
    std_dev = np.std(returns)
    mean = np.mean(returns)
    cvar = (alpha**-1 * norm.pdf(norm.ppf(alpha)) * std_dev - mean) * np.sqrt(days)
    return cvar
if __name__ == "__main__":
    returns = np.random.randn(1000)
    confidence_level = 95
    days = 1
    var_hist_result = var_hist(returns, confidence_level, days)
    var_vcov_result = var_vcov(returns, confidence_level, days)
    print("Historical VaR:", var_hist_result)
    print("Variance-Covariance VaR:", var_vcov_result)
    cvar_hist_result = cvar_hist(returns, var_hist_result, days)
    cvar_vcov_result = cvar_vcov(returns, confidence_level, days)
    print("Historical CVaR:", cvar_hist_result)
    print("Variance-Covariance CVaR:", cvar_vcov_result)