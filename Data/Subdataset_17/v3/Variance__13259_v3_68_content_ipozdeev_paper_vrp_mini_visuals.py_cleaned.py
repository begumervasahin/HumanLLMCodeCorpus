import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D
from cycler import cycler
import seaborn as sns
n_red = "
n_blue = "
n_green = "
n_gray = "
n_black = "
n_palette = [n_red, n_blue, n_green, n_gray]
colorblind_palette = sns.color_palette("colorblind", 9)
colorblind_cmap = LinearSegmentedColormap.from_list("colorblind_cmap", colorblind_palette)
plt.rcParams['axes.prop_cycle'] = cycler(color=colorblind_palette)
blue_hsluv = 248.2
red_hsluv = 26.8
heatmap_cmap = sns.diverging_palette(blue_hsluv, red_hsluv, 85, 54, n=15, as_cmap=True)
figsize_1 = (6.5, 3)
figsize_2 = (6.5, 6)
def set_visuals():
    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 10,
        'figure.figsize': figsize_1,
        'xtick.labelsize': 10,
        'ytick.alignment': 'center',
        'axes.grid': True,
        'grid.linestyle': '-',
        'grid.alpha': 0.75,
        'legend.fontsize': 10
    })
def add_line(color='black', lw=1, linestyle='-', label=''):
    return Line2D([0], [0], color=color, linewidth=lw, linestyle=linestyle, label=label)
set_visuals()
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()