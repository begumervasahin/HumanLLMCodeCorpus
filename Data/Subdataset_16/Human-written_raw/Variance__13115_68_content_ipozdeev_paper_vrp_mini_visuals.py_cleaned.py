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
b10 = sns.diverging_palette(a1, a2, 85, 54,
                                     b11 = 15, as_cmap=True)
b12 = ((8.5 - 2), ((11.0 - 2) / 3))
b13 = ((8.5 - 2), (11.0 - 2) / 1.5)
def fonk1():
    b14 = {
        "family": "serif",
        "size": 10}
    b15 = {
        "figsize": b12}
    b16 = {
        "labelsize": 10}
    b17 = {
        "alignment": "center"
    }
    b18 = {
        "grid": True}
    b19 = {
        "linestyle": '-',
        "alpha": 0.75}
    b20 = {
        "fontsize": 10}
    plt.rc("xtick", **b16)
    plt.rc("ytick", **b17)
    plt.rc("figure", **b15)
    plt.rc("font", **b14)
    plt.rc("axes", **b18)
    plt.rc("grid", **b19)
    plt.rc("legend", **b20)
def fonk2(**kwargs):
    b21 = Line2D([0], [0], **kwargs)
    return b21