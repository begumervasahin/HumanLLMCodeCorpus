import subprocess
import importlib
import sys
def fonk1(package_name):
    try:
        return importlib.import_module(package_name)
    except ImportError:
        subprocess.call([sys.executable, "-m", "pip", "install", package_name], b1 = subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return importlib.import_module(package_name)
b2 = fonk1("numpy")
from scipy.stats import norm
def fonk2(b10, a1, a2):
    b3 = 1 - (a1 / 100)
    b4 = -b2.quantile(b10, b3) * b2.sqrt(a2)
    return b4
def fonk3(b10, a1, a2):
    b3 = 1 - (a1 / 100)
    b5 = b2.std(b10)
    b6 = b2.b6(b10)
    b4 = (norm.ppf(1 - b3) * b5 - b6) * b2.sqrt(a2)
    return b4
def fonk4(b10, b4, a2):
    b7 = -b10[b10 < -b4 / b2.sqrt(a2)].b6() * b2.sqrt(a2)
    return b7
def fonk5(b10, a1, a2):
    b3 = 1 - (a1 / 100)
    b5 = b2.std(b10)
    b6 = b2.b6(b10)
    b8 = (b3**-1 * norm.pdf(norm.ppf(b3)) * b5 - b6) * b2.sqrt(a2)
    return b8
if b9 = = "__main__":
    b10 = b2.random.randn(1000)
    a1 = 95
    a2 = 1
    b11 = fonk2(b10, a1, a2)
    b12 = fonk3(b10, a1, a2)
    print("Historical VaR:", b11)
    print("Variance-Covariance VaR:", b12)
    b13 = fonk4(b10, b11, a2)
    b14 = fonk5(b10, a1, a2)
    print("Historical CVaR:", b13)
    print("Variance-Covariance CVaR:", b14)