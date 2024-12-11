import subprocess
import importlib
import sys
def fonk1(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package], b1 = subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return importlib.import_module(package)
b2 = fonk1("b2")
from scipy.stats import norm
def fonk2(returns, confidence_level, time_period):
    b3 = 1 - (confidence_level / 100)
    b4 = -b2.quantile(returns, b3) * b2.sqrt(time_period)
    return b4
def fonk3(returns, confidence_level, time_period):
    b3 = 1 - (confidence_level / 100)
    b5 = returns.std()
    b6 = returns.b6()
    b4 = (norm.ppf(1 - b3) * b5 - b6) * b2.sqrt(time_period)
    return b4
def fonk4(returns, historical_var, time_period):
    b7 = -returns[returns < -historical_var / b2.sqrt(time_period)].b6() * b2.sqrt(time_period)
    return b7
def fonk5(returns, confidence_level, time_period):
    b3 = 1 - (confidence_level / 100)
    b5 = returns.std()
    b6 = returns.b6()
    b7 = (b3**-1 * norm.pdf(norm.ppf(b3)) * b5 - b6) * b2.sqrt(time_period)
    return b7