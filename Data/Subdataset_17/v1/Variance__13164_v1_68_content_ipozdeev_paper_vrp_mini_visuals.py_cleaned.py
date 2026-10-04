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
cblind_palette = sns.color_palette("colorblind", 9)
cblind_cmap = LinearSegmentedColormap.from_list("cmap", cblind_palette)
plt.rcParams['axes.prop_cycle'] = cycler(color=cblind_palette)
n_blue_hsluv = 248.2
n_red_hsluv = 26.8
heatmap_cmap = sns.diverging_palette(n_blue_hsluv, n_red_hsluv, 85, 54, n=15, as_cmap=True)
figsize_1 = (8.5 - 2, (11.0 - 2) / 3)
figsize_2 = (8.5 - 2, (11.0 - 2) / 1.5)
def set_visuals():
    font_settings = {
        "family": "serif",
        "size": 10
    }
    fig_settings = {
        "figsize": figsize_1
    }
    xtick_settings = {
        "labelsize": 10
    }
    ytick_settings = {
        "alignment": "center"
    }
    axes_settings = {
        "grid": True
    }
    grid_settings = {
        "linestyle": '-',
        "alpha": 0.75
    }
    legend_settings = {
        "fontsize": 10
    }
    plt.rc("xtick", **xtick_settings)
    plt.rc("ytick", **ytick_settings)
    plt.rc("figure", **fig_settings)
    plt.rc("font", **font_settings)
    plt.rc("axes", **axes_settings)
    plt.rc("grid", **grid_settings)
    plt.rc("legend", **legend_settings)
def add_line(**kwargs):
    return Line2D([0], [0], **kwargs)
set_visuals()
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()