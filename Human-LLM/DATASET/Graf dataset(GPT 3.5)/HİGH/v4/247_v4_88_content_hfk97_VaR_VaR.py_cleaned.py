import subprocess
import importlib
import sys
def fonk1(package):
    try:
        return importlib.import_module(package)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package], b1 = subprocess.DEVNULL,
                        b2 = subprocess.DEVNULL)
        return importlib.import_module(package)
b3 = fonk1("b3")
b4 = fonk1("b4")
from b4.stats import norm
def fonk2(returns, confidence, days):
    b5 = (1 - (confidence / 100))
    b6 = -b3.quantile(returns, b5)
    b6 *= b3.sqrt(days)
    return b6
def fonk3(returns, confidence, days):
    b7 = returns.std()
    b8 = returns.b8()
    b5 = (1 - (confidence / 100))
    b9 = norm.ppf(1 - b5) * b7 - b8
    b9 *= b3.sqrt(days)
    return b9
def fonk4(returns, b6, days):
    b6 /= b3.sqrt(days)
    b10 = -returns[returns < -b6].b8()
    b10 *= b3.sqrt(days)
    return b10
def fonk5(returns, confidence, days):
    b5 = (1 - (confidence / 100))
    b7 = returns.std()
    b8 = returns.b8()
    b11 = b5**-1 * norm.pdf(norm.ppf(b5)) * b7 - b8
    b11 *= b3.sqrt(days)
    return b11