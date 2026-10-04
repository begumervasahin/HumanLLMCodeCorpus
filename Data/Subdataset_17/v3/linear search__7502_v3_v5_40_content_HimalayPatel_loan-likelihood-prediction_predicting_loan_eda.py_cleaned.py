import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def load_dataset(file_path):
    return pd.read_csv(file_path)
def remove_columns(dataset, columns_to_drop):
    return dataset.drop(columns=columns_to_drop)
def plot_histograms(dataset):
    fig, axes = plt.subplots(nrows=6, ncols=3, figsize=(15, 12))
    fig.suptitle('Histograms of Numerical Columns', fontsize=20)
    for index, ax in enumerate(axes.flat):
        if index < len(dataset.columns):
            column_name = dataset.columns[index]
            ax.set_title(column_name)
            unique_values = np.size(dataset[column_name].unique())
            bins = min(unique_values, 100)
            ax.hist(dataset[column_name], bins=bins, color='blue')
        else:
            ax.axis('off')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
def plot_correlation_with_target(dataset, target_column):
    correlation_with_target = dataset.corrwith(target_column)
    correlation_with_target.plot.bar(figsize=(20, 10), title="Correlation with e_signed", fontsize=15, rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix(dataset):
    sns.set(style="white")
    correlation_matrix = dataset.corr()
    mask = np.zeros_like(correlation_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=(18, 15))
    color_map = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
if __name__ == "__main__":
    file_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
    dataset = load_dataset(file_path)
    columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
    dataset_filtered = remove_columns(dataset, columns_to_drop)
    plot_histograms(dataset_filtered)
    plot_correlation_with_target(dataset_filtered, dataset['e_signed'])
    plot_correlation_matrix(dataset_filtered)