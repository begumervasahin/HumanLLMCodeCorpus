
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
dataset = pd.read_csv(file_path)
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_cleaned = dataset.drop(columns=columns_to_drop)
def plot_histograms(data, figsize=(15, 12)):
    fig, axes = plt.subplots(nrows=6, ncols=3, figsize=figsize)
    fig.suptitle('Histograms of Numerical Columns', fontsize=20)
    for i, column in enumerate(data.columns):
        ax = axes[i
        unique_values_count = min(np.size(data[column].unique()), 100)
        ax.hist(data[column], bins=unique_values_count, color='blue')
        ax.set_title(column)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
plot_histograms(dataset_cleaned)
def plot_correlation_with_target(data, target, figsize=(20, 10)):
    correlation_with_target = data.corrwith(target)
    correlation_with_target.plot.bar(figsize=figsize, title="Correlation with e_signed", fontsize=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
plot_correlation_with_target(dataset_cleaned, dataset['e_signed'])
def plot_correlation_heatmap(data, figsize=(18, 15), vmax=0.4):
    sns.set(style="white")
    correlation_matrix = data.corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    fig, ax = plt.subplots(figsize=figsize)
    color_map = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=vmax, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.title("Correlation Matrix", fontsize=20)
    plt.show()
plot_correlation_heatmap(dataset_cleaned)