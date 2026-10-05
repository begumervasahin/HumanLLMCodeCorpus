import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset = pd.read_csv("C:\\Users\\himal\\Desktop\\Machine Learning Practicals\\P5- Predicting the likelihood of e-signing a loan based on Financial History\\P39-Financial-Data.csv")
columns_to_drop = ['entry_id', 'pay_schedule', 'e_signed']
dataset_cleaned = dataset.drop(columns=columns_to_drop)
fig = plt.figure(figsize=(15, 12))
plt.suptitle('Histograms of Numerical Columns', fontsize=20)
for i, column in enumerate(dataset_cleaned.columns):
    plt.subplot(6, 3, i + 1)
    current_subplot = plt.gca()
    current_subplot.set_title(column)
    unique_values_count = np.size(dataset_cleaned[column].unique())
    if unique_values_count >= 100:
        unique_values_count = 100
    plt.hist(dataset_cleaned[column], bins=unique_values_count, color='blue')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
correlation_with_e_signed = dataset_cleaned.corrwith(dataset['e_signed'])
correlation_with_e_signed.plot.bar(
    figsize=(20, 10), title="Correlation with e_signed", fontsize=15,
    rot=45, grid=True)
plt.tight_layout()
plt.show()
sns.set(style="white")
correlation_matrix = dataset_cleaned.corr()
mask = np.zeros_like(correlation_matrix, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
fig, ax = plt.subplots(figsize=(18, 15))
color_map = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(correlation_matrix, mask=mask, cmap=color_map, vmax=0.4, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.suptitle("Correlation Matrix")
plt.show()