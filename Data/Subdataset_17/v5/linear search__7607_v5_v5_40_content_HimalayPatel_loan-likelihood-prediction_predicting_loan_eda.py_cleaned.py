import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
dataset = pd.read_csv(file_path)
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_filtered = dataset.drop(columns=columns_to_drop)
def plot_histograms(data, n_cols=3):
    num_columns = data.select_dtypes(include=[np.number]).columns
    n_rows = (len(num_columns) + n_cols - 1)
    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=(15, 12))
    fig.suptitle('Histograms of Numerical Columns', fontsize=20)
    for index, column_name in enumerate(num_columns):
        row, col = divmod(index, n_cols)
        ax = axes[row, col]
        ax.set_title(column_name)
        unique_values = np.size(data[column_name].unique())
        bins = min(unique_values, 100)
        ax.hist(data[column_name], bins=bins, color='blue')
    for ax in axes.flat[len(num_columns):]:
        ax.axis('off')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
def plot_correlation_with_target(data, target_column):
    correlation_with_target = data.corrwith(dataset[target_column])
    correlation_with_target.plot.bar(figsize=(20, 10), title=f"Correlation with {target_column}", fontsize=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix(data):
    sns.set(style="white")
    correlation_matrix = data.corr()
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    fig, ax = plt.subplots(figsize=(18, 15))
    color_map = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True)
    plt.title("Correlation Matrix", fontsize=20)
    plt.show()
plot_histograms(dataset_filtered)
plot_correlation_with_target(dataset_filtered, 'e_signed')
plot_correlation_matrix(dataset_filtered)