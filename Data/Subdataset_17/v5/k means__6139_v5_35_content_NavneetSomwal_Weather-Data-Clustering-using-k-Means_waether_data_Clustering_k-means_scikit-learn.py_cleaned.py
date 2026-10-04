
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle, islice
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pandas.plotting import parallel_coordinates
def load_and_sample_data(file_path, sample_rate=10):
    data = pd.read_csv(file_path)
    print(f"Original data shape: {data.shape}")
    sampled_data = data[data['rowID'] % sample_rate == 0]
    print(f"Sampled data shape: {sampled_data.shape}")
    return sampled_data
def preprocess_data(df):
    df.drop(['rain_accumulation', 'rain_duration'], axis=1, inplace=True)
    rows_before = df.shape[0]
    df.dropna(inplace=True)
    rows_after = df.shape[0]
    print(f"Rows dropped due to NA: {rows_before - rows_after}")
    return df
def standardize_features(df, feature_cols):
    select_df = df[feature_cols]
    print(f"Selected features: {select_df.columns.tolist()}")
    X = StandardScaler().fit_transform(select_df)
    return X
def perform_kmeans_clustering(X, n_clusters=12, random_state=42):
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    model = kmeans.fit(X)
    print("KMeans model:", model)
    return model
def create_centers_df(features, centers):
    col_names = list(features) + ['prediction']
    data = [np.append(center, idx) for idx, center in enumerate(centers)]
    centers_df = pd.DataFrame(data, columns=col_names)
    centers_df['prediction'] = centers_df['prediction'].astype(int)
    return centers_df
def parallel_plot(data, y_label='prediction', title='Parallel Coordinates Plot'):
    colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
    plt.figure(figsize=(15, 8))
    plt.gca().axes.set_ylim([-3, +3])
    parallel_coordinates(data, y_label, color=colors, marker='o')
    plt.title(title)
    plt.show()
file_path = './weather/minute_weather.csv'
data = load_and_sample_data(file_path)
data_summary = data.describe().transpose()
print(data_summary)
preprocessed_data = preprocess_data(data)
features = ['air_pressure', 'air_temp', 'avg_wind_direction', 'avg_wind_speed', 'max_wind_direction', 'max_wind_speed', 'relative_humidity']
X = standardize_features(preprocessed_data, features)
kmeans_model = perform_kmeans_clustering(X)
centers = kmeans_model.cluster_centers_
P = create_centers_df(features, centers)
print(P)
parallel_plot(P[P['relative_humidity'] < -0.5], title='Relative Humidity < -0.5')
parallel_plot(P[P['air_temp'] > 0.5], title='Air Temperature > 0.5')
parallel_plot(P[(P['relative_humidity'] > 0.5) & (P['air_temp'] < 0.5)], title='Relative Humidity > 0.5 and Air Temperature < 0.5')