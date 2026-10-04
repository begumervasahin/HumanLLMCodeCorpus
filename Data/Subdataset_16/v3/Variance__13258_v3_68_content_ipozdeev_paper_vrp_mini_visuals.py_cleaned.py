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
b8 = LinearSegmentedColormap.from_list("b8", b7)
plt.rcParams['axes.prop_cycle'] = cycler(b9 = b7)
a1 = 248.2
a2 = 26.8
b10 = sns.diverging_palette(a1, a2, 85, 54, n=15, as_cmap=True)
b11 = (6.5, 3)
b12 = (6.5, 6)
def fonk1():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'figure.figsize': b11,
        'xtick.labelsize': 10,
        'ytick.alignment': 'center',
        'axes.grid': True,
        'grid.linestyle': '-',
        'grid.alpha': 0.75,
        'legend.fontsize': 10
    })
def fonk2(b9 = 'black', lw=1, linestyle='-', label=''):
    return Line2D([0], [0], b9 = b9, linewidth=lw, linestyle=linestyle, label=label)
fonk1()
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()