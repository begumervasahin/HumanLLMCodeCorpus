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
b3 = fonk1("numpy")
b4 = fonk1("b4")
from b4.stats import norm
def fonk2(b12, confidence, a2):
    b5 = (1 - (confidence / 100))
    b6 = -b3.quantile(b12, b5)
    b6 *= b3.sqrt(a2)
    return b6
def fonk3(b12, confidence, a2):
    b7 = b12.std()
    b8 = b12.b8()
    b5 = (1 - (confidence / 100))
    b9 = norm.ppf(1 - b5) * b7 - b8
    b9 *= b3.sqrt(a2)
    return b9
def fonk4(b12, b6, a2):
    b6 /= b3.sqrt(a2)
    b10 = -b12[b12 < -b6].b8()
    b10 *= b3.sqrt(a2)
    return b10
def fonk5(b12, confidence, a2):
    b5 = (1-(confidence/100))
    b7 = b12.std()
    b8 = b12.b8()
    b11 = b5**-1 * norm.pdf(norm.ppf(b5))*b7-b8
    b11 *= b3.sqrt(a2)
    return b11
b12 = b3.random.randn(1000)
a1 = 95
a2 = 1
b13 = fonk2(b12, a1, a2)
b14 = fonk3(b12, a1, a2)
print("Historical VaR:", b13)
print("Variance-Covariance VaR:", b14)
b15 = fonk4(b12, b13, a2)
b16 = fonk5(b12, a1, a2)
print("Historical CVaR:", b15)
print("Variance-Covariance CVaR:", b16)