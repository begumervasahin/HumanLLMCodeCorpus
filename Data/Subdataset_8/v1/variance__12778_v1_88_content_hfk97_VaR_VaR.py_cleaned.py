import subprocess
import importlib
import sys
def getpack(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL)
        return importlib.import_module(package)
np = getpack("numpy")
scipy = getpack("scipy")
from scipy.stats import norm
def var_hist(returns, confidence, days):
    alpha = (1 - (confidence / 100))
    var_hist = -np.quantile(returns, alpha)
    var_hist *= np.sqrt(days)
    return var_hist
def var_vcov(returns, confidence, days):
    std_dev = returns.std()
    mean = returns.mean()
    alpha = (1 - (confidence / 100))
    var_var_covar = norm.ppf(1 - alpha) * std_dev - mean
    var_var_covar *= np.sqrt(days)
    return var_var_covar
def cvar_hist(returns, var_hist, days):
    var_hist /= np.sqrt(days)
    es_hist = -returns[returns < -var_hist].mean()
    es_hist *= np.sqrt(days)
    return es_hist
def cvar_vcov(returns, confidence, days):
    alpha = (1-(confidence/100))
    std_dev = returns.std()
    mean = returns.mean()
    es_var_covar = alpha**-1 * norm.pdf(norm.ppf(alpha))*std_dev-mean
    es_var_covar *= np.sqrt(days)
    return es_var_covar
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