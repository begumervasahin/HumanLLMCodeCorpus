import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from cycler import cycler
import seaborn as sns
b1 = "
b2 = "
b3 = "
b4 = "
b5 = "
b6 = [b1, b2, b3, b4]
b7 = sns.color_palette("colorblind", 9)
b8 = LinearSegmentedColormap.from_list("cmap", b7)
plt.rcParams['axes.prop_cycle'] = cycler(b9 = b7)
a1 = 248.2
a2 = 26.8
b10 = sns.diverging_palette(a1, a2, 85, 54, n=15, as_cmap=True)
b11 = (6.5, 3)
b12 = (6.5, 6)
def fonk1():
    b13 = {
        "family": "serif",
        "size": 10
    }
    b14 = {
        "figsize": b11
    }
    b15 = {
        "labelsize": 10
    }
    b16 = {
        "alignment": "center"
    }
    b17 = {
        "grid": True
    }
    b18 = {
        "linestyle": '-',
        "alpha": 0.75
    }
    b19 = {
        "fontsize": 10
    }
    plt.rc("xtick", **b15)
    plt.rc("ytick", **b16)
    plt.rc("figure", **b14)
    plt.rc("font", **b13)
    plt.rc("axes", **b17)
    plt.rc("grid", **b18)
    plt.rc("legend", **b19)
def fonk2(**kwargs):
    return Line2D([0], [0], **kwargs)