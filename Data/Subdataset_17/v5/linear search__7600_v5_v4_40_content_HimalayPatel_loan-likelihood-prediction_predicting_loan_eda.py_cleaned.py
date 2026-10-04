import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
dataset = pd.read_csv(dataset_path)
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_cleaned = dataset.drop(columns=columns_to_drop)
def plot_histograms(df, figsize=(15, 12)):
    fig, axes = plt.subplots(nrows=6, ncols=3, figsize=figsize)
    fig.suptitle('Histograms of Numerical Columns', fontsize=20)
    for i, ax in enumerate(axes.flatten()):
        if i < df.shape[1]:
            col = df.columns[i]
            unique_values = np.size(df[col].unique())
            bins = min(unique_values, 100)
            ax.hist(df[col], bins=bins, color='blue')
            ax.set_title(col)
        else:
            ax.axis('off')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
plot_histograms(dataset_cleaned)
def plot_correlation_with_target(df, target, figsize=(20, 10)):
    plt.figure(figsize=figsize)
    df.corrwith(target).plot.bar(
        title="Correlation with e_signed", fontsize=15, rot=45, grid=True
    )
    plt.tight_layout()
    plt.show()
plot_correlation_with_target(dataset_cleaned, dataset['e_signed'])
def plot_correlation_heatmap(df, figsize=(18, 15), vmax=0.4):
    sns.set(style="white")
    correlation_matrix = df.corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    fig, ax = plt.subplots(figsize=figsize)
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=cmap, vmax=vmax, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
plot_correlation_heatmap(dataset_cleaned)