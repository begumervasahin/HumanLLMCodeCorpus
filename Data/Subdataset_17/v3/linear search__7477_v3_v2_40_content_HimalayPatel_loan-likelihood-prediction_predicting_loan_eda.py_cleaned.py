import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def load_dataset(file_path):
    return pd.read_csv(file_path)
def drop_columns(dataframe, columns_to_remove):
    return dataframe.drop(columns=columns_to_remove)
def plot_histograms(dataframe):
    num_columns = dataframe.shape[1]
    num_rows = (num_columns
    fig = plt.figure(figsize=(15, 12))
    plt.suptitle('Histograms of Numerical Columns', fontsize=20)
    for index, column in enumerate(dataframe.columns):
        plt.subplot(num_rows, 3, index + 1)
        plt.gca().set_title(column)
        num_unique_values = np.size(dataframe[column].unique())
        num_bins = min(num_unique_values, 100)
        plt.hist(dataframe[column], bins=num_bins, color='blue')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
def plot_correlation_with_target(dataframe, target_series):
    correlation_with_target = dataframe.corrwith(target_series)
    correlation_with_target.plot.bar(
        figsize=(20, 10), title="Correlation with e_signed", fontsize=15,
        rot=45, grid=True)
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix(dataframe):
    sns.set(style="white")
    correlation_matrix = dataframe.corr()
    mask = np.zeros_like(correlation_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True
    fig, ax = plt.subplots(figsize=(18, 15))
    color_map = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    plt.suptitle("Correlation Matrix")
    plt.show()
def main():
    dataset_path = "C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv"
    columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
    dataset = load_dataset(dataset_path)
    cleaned_dataset = drop_columns(dataset, columns_to_drop)
    plot_histograms(cleaned_dataset)
    plot_correlation_with_target(cleaned_dataset, dataset['e_signed'])
    plot_correlation_matrix(cleaned_dataset)
if __name__ == "__main__":
    main()