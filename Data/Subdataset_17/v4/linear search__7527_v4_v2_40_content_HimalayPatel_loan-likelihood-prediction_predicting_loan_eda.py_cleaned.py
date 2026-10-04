import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def load_and_clean_data(filepath, columns_to_drop):
    dataset = pd.read_csv(filepath)
    cleaned_dataset = dataset.drop(columns=columns_to_drop)
    return cleaned_dataset
def plot_histograms(df, figsize=(15, 12), suptitle='Histograms of Numerical Columns'):
    fig = plt.figure(figsize=figsize)
    plt.suptitle(suptitle, fontsize=20)
    for i, column in enumerate(df.columns):
        plt.subplot(6, 3, i + 1)
        plt.title(column)
        unique_values_count = np.size(df[column].unique())
        bins = min(unique_values_count, 100)
        plt.hist(df[column], bins=bins, color='blue')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
def plot_correlation_with_target(df, target_column, figsize=(20, 10), title="Correlation with Target"):
    correlation_with_target = df.corrwith(df[target_column])
    correlation_with_target.plot.bar(figsize=figsize, title=title, fontsize=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix_heatmap(df, title="Correlation Matrix", figsize=(18, 15)):
    sns.set(style="white")
    correlation_matrix = df.corr()
    mask = np.zeros_like(correlation_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=figsize)
    color_map = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle(title)
    plt.show()
filepath = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_cleaned = load_and_clean_data(filepath, columns_to_drop)
plot_histograms(dataset_cleaned)
plot_correlation_with_target(dataset_cleaned, 'e_signed')
plot_correlation_matrix_heatmap(dataset_cleaned)