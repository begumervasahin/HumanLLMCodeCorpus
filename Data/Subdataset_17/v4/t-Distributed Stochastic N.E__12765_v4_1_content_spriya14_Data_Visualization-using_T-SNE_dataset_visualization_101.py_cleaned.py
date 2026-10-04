
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
data_url = "https:
data = pd.read_csv(data_url)
print("Initial Data Preview:")
print(data.head())
missing_counts = data.isnull().sum()
columns_without_null = missing_counts[missing_counts == 0].index
data_cleaned = data[columns_without_null]
data_cleaned = data_cleaned.iloc[:, 7:]
print("\nRemaining Columns After Cleaning:")
print(data_cleaned.columns)
X = data_cleaned.iloc[:, :-1].values
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)
y = data_cleaned.iloc[:, -1].values
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
class_labels = np.unique(y)
print("\nClass Labels:")
print(class_labels)
test_size = 0.1
X_train, X_test, y_train, y_test = train_test_split(X_standardized, y_encoded, test_size=test_size, random_state=0)
tsne = TSNE(n_components=2, random_state=0)
X_test_2d = tsne.fit_transform(X_test)
markers = ['s', 'd', 'o', '^', 'v']
colors = ['red', 'blue', 'lightgreen', 'purple', 'cyan']
color_map = dict(zip(np.unique(y_test), colors))
plt.figure(figsize=(10, 8))
for idx, class_label in enumerate(np.unique(y_test)):
    plt.scatter(X_test_2d[y_test == class_label, 0], X_test_2d[y_test == class_label, 1],
                c=color_map[class_label], marker=markers[idx], label=label_encoder.inverse_transform([class_label])[0])
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.legend(loc='upper left')
plt.title('t-SNE Visualization of Test Data')
plt.show()
def main():
    pass
if __name__ == "__main__":
    main()